from modello_base import ModelloBase
import pandas as pd
from scipy.stats import chi2_contingency, contingency, spearmanr
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

variabili_da_droppare = ['rank','latitude_country','longitude_country','date','title','firstName','lastName','status',
                         'birthDate','birthYear','birthMonth','birthDay','population_country','gross_tertiary_education_enrollment',
                         'gross_primary_education_enrollment_country','life_expectancy_country', 'tax_revenue_country_country',
                         'total_tax_rate_country','gdp_country','cpi_change_country','cpi_country','residenceStateRegion','category']

variabili_da_droppare_genere = ["finalWorth","personName","age","country","city","source","industries","countryOfCitizenship","countryOfCitizenship","organization","selfMade","state",'rank','latitude_country','longitude_country','date','title','firstName','lastName','status',
                         'birthDate','birthYear','birthMonth','birthDay','population_country','gross_tertiary_education_enrollment',
                         'gross_primary_education_enrollment_country','life_expectancy_country', 'tax_revenue_country_country',
                         'total_tax_rate_country','gdp_country','cpi_change_country','cpi_country','residenceStateRegion','category']

variabili_da_droppare_industrie = ["finalWorth","personName","age","country","city","source","gender","countryOfCitizenship","countryOfCitizenship","organization","selfMade","state",'rank','latitude_country','longitude_country','date','title','firstName','lastName','status',
                         'birthDate','birthYear','birthMonth','birthDay','population_country','gross_tertiary_education_enrollment',
                         'gross_primary_education_enrollment_country','life_expectancy_country', 'tax_revenue_country_country',
                         'total_tax_rate_country','gdp_country','cpi_change_country','cpi_country','residenceStateRegion','category']

colonne_da_rinominare = {
    "finalWorth": "patrimonio_finale",
    "personName": "nome_persona",
    "age": "eta",
    "country": "paese",
    "city": "citta",
    "source": "fonte_reddito",
    "industries": "industrie",
    "countryOfCitizenship": "paese_cittadinanza",
    "organization": "organizzazione",
    "selfMade": "self_made",
    "gender": "genere",
    "state": "stato"}

class ModelloBillionaire(ModelloBase):

    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato = self.sistemazione_dataframe()
        self.dataframe_sistemato_genere = self.sistemazione_dataframe_genere()
        self.dataframe_sistemato_industrie = self.sistemazione_dataframe_industrie()

    def sistemazione_dataframe(self):

        df_sistemato = self.dataframe.drop(variabili_da_droppare, axis=1)
        df_sistemato["age"] = df_sistemato["age"].fillna(df_sistemato["age"].median())

        # conversione di tipo float in tipo int
        df_sistemato["age"] = df_sistemato["age"].astype(int)

        df_sistemato = df_sistemato.rename(columns=colonne_da_rinominare)

        # Creazione colonna "fascia_eta"
        bins = [0, 39, 60, df_sistemato["eta"].max()]
        labels = ["Under 40", "40-60", "Over 60"]
        df_sistemato["fascia_eta"] = pd.cut(df_sistemato["eta"], bins=bins, labels=labels, right=True)

        df_sistemato["codice_fascia_eta"] = df_sistemato["fascia_eta"].cat.codes

        df_sistemato['genere'] = df_sistemato['genere'].map({'M':1, 'F': 2})
        df_sistemato['industrie'] = df_sistemato['industrie'].map({'Fashion & Retail':1,
                                                            'Automotive': 2,
                                                            'Technology': 3,
                                                            'Finance & Investments': 4,
                                                            'Media & Entertainment': 5,
                                                            'Telecom': 6,
                                                            'Diversified': 7,
                                                            'Food & Beverage': 8,
                                                            'Logistics': 9,
                                                            'Gambling & Casinos': 10,
                                                            'Manufacturing': 11,
                                                            'Real Estate': 12,
                                                            'Metals & Mining': 13,
                                                            'Energy': 14,
                                                            'Healthcare': 15,
                                                            'Service': 16,
                                                            'Construction & Engineering': 17,
                                                            'Sports': 18})

        return df_sistemato

    def sistemazione_dataframe_genere(self):

        df_sistemato = self.dataframe.drop(variabili_da_droppare_genere, axis=1)
        valori_univoci = df_sistemato["gender"].dropna().unique()
        df_sistemato = pd.DataFrame(valori_univoci, columns=['gender'])

        return df_sistemato

    def sistemazione_dataframe_industrie(self):

        df_sistemato = self.dataframe.drop(variabili_da_droppare_industrie, axis=1)
        valori_univoci = df_sistemato["industries"].dropna().unique()
        df_sistemato = pd.DataFrame(valori_univoci, columns=['industries'])

        return df_sistemato

    def tabella_contingenza(self,column, target):
        # generazione e stampa tabella di contingenza
        tabella_contingenza = pd.crosstab(self.dataframe_sistemato[column], self.dataframe_sistemato[target])

        print(f'TABELLA DI CONTINGENZA {column} - {target}: ', tabella_contingenza, sep='\n')
        # test chi quadro e stampa esito
        chi2, p, dof, expected = chi2_contingency(tabella_contingenza)
        print(f'Il p-value risultante dal test chi quadro sulla tabella di contingenza {column} - {target} è: {p}')
        print(f'Notazione non scientifica del p-value: {format(p, '.53f')}')

        cramer = contingency.association(tabella_contingenza, method='cramer')

        print(f'L\'indice di Cramer calcolato sulla tabella di contingenza {column} - {target} è pari a: {cramer}')

        # L'indice di Cramer calcolato sulla tabella di contingenza genere - categorie è pari a: 0.11417300576850022

        # di base da 0 a 0.1 è una correlazione debole, da 0.1 a 0.3 è una correlazione bassa, da 0.3 a 0.5 è una correlazione moderata
        # da 0.5 a 0.7 è una correlazione alta, da 0.7 a 0.9 è una correlazione molto alta, da 0.9 a 1 è una correlazione perfetta

        return tabella_contingenza


    # metodo per ottenere correlazione di Spearman (correlazione tra variabile quantitativa e categoriale)
    def correlazione_spearman(self, column, target):
        spearman_corr, p = spearmanr(self.dataframe_sistemato[column], self.dataframe_sistemato[target])
        print(f'La correlazione di Spearman risultante tra {column} e {target} risulta pari a: {spearman_corr}')
        print(f'Il p-value risultante dal test chi quadro sulla tabella di contingenza {column} - {target} è: {p}')

    # Nessun correlazione
    # La correlazione di Spearman risultante tra fascia_eta e patrimonio_finale risulta pari a: 0.09659820893002695
    # Il p-value risultante dal test chi quadro sulla tabella di contingenza fascia_eta - patrimonio_finale è: 6.606515487681456e-07

    def regressione_lineare_semplice(self):

        # Definizione target e regressore
        y = self.dataframe_sistemato[["patrimonio_finale"]].values.reshape(-1, 1)  # TARGET
        x = self.dataframe_sistemato[["eta"]].values.reshape(-1, 1)  # REGRESSORE

        # Standardizzazione
        scaler = StandardScaler()
        x_scaled = scaler.fit_transform(x)

        # Creazione e addestramento del modello
        regressione = LinearRegression()
        regressione.fit(x_scaled, y)

        # Punteggio del modello
        print("\n****** PUNTEGGIO MODELLO REGRESSIONE *****")
        print(regressione.score(x_scaled, y))

        # Predizione della retta di regressione
        retta_regressione = regressione.predict(x_scaled)

        # Grafico
        plt.scatter(x, y, label="Osservazioni", s=10, color="steelblue")
        plt.plot(x, retta_regressione, color="darkred", label="Regressione Lineare", linewidth=1.5)
        plt.title("Regressione Lineare tra Età e Patrimonio")
        plt.xlabel("Età")
        plt.ylabel("Patrimonio Finale (milioni di dollari)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()


# utilizzo modello

modello = ModelloBillionaire('../dataset/billionaires_statistics_dataset.csv')
#modello.analisi_generali(modello.dataframe_sistemato)

modello.tabella_contingenza('genere','industrie')
print('\n')
modello.correlazione_spearman('codice_fascia_eta','patrimonio_finale')
modello.regressione_lineare_semplice()
modello.analisi_valori_univoci(modello.dataframe_sistemato)
# creazione file csv con modifiche fatte
modello.dataframe_sistemato.to_csv("../dataset_sistemato/billionaires_sistemato.csv", index=False)
# modello.dataframe_sistemato_genere.to_csv("../dataset_sistemato/billionaires_sistemato_genere.csv", index=False)
# modello.dataframe_sistemato_industrie.to_csv("../dataset_sistemato/billionaires_sistemato_industrie.csv", index=False)