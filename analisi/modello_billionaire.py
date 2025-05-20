from modello_base import ModelloBase
import pandas as pd
from scipy.stats import chi2_contingency, contingency, spearmanr
import matplotlib.pyplot as plt

variabili_da_droppare = ['rank','latitude_country','longitude_country','date','title','firstName','lastName','status',
                         'birthDate','birthYear','birthMonth','birthDay','population_country','gross_tertiary_education_enrollment',
                         'gross_primary_education_enrollment_country','life_expectancy_country', 'tax_revenue_country_country',
                         'total_tax_rate_country','gdp_country','cpi_change_country','cpi_country','residenceStateRegion']

class ModelloBillionaire(ModelloBase):

    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato = self.sistemazione_dataframe()

    def sistemazione_dataframe(self):

        df_sistemato = self.dataframe.drop(variabili_da_droppare, axis=1)

        df_sistemato["age"] = df_sistemato["age"].fillna(df_sistemato["age"].median())
        df_sistemato["age"] = df_sistemato["age"].astype(int)

        return df_sistemato

# utilizzo modello

modello = ModelloBillionaire('../dataset/billionaires_statistics_dataset.csv')
modello.analisi_generali(modello.dataframe_sistemato)
# modello.analisi_valori_univoci(modello.dataframe_sistemato)
# creazione file csv con modifiche fatte
# modello.dataframe_sistemato.to_csv("../dataset_sistemato/billionaires_sistemato.csv", index=False)
