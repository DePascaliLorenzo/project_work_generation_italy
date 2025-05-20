from abc import ABC

# definizione classe astratta per centralizzazione operazioni comuni
class ModelloBase(ABC):

    # metodo per ottenimento informazioni generali
    @staticmethod
    def analisi_generali(df):
        print('***** ANALISI GENERALI DATAFRAME *****', df.to_string(), sep='\n')
        print('Prime cinque osservazioni: ', df.head().to_string(), sep='\n')
        print('Ultime cinque osservazioni: ', df.tail().to_string(), sep='\n')
        print('Informazioni generali dataframe:')
        df.info()

    # metodo per controllo valori univoci variabili categoriali
    @staticmethod
    def analisi_valori_univoci(df, variabili_da_droppare = None):
        print('***** VALORI UNIVOCI DATAFRAME *****')
        if variabili_da_droppare:
            df = df.drop(variabili_da_droppare, axis=1)
        for col in df.columns:
            print(f'In colonna {col} abbiamo: {df[col].nunique()} valori univoci')
            for value in df[col].unique():
                print(value)

    # metodo per analisi indici statistici
    @staticmethod
    def analisi_indici_statistici(df):
        print('***** INDICI STATISTICI DATAFRAME *****')
        # indici generali variabili quantitative del df
        indici_generali = df.describe()
        print('Indici statistici generali variabili quantitative: ',indici_generali.to_string(), sep = '\n')
        # moda variabili quantitative e categoriali
        for col in df.columns:
            print(f'Moda colonna {col}: ', df[col].mode().iloc[0])

    # metodo per individuazione outliers colonna
    @staticmethod
    def individuazione_outliers(df, variabili_da_droppare = None):
        print('***** INDIVIDUAZIONE OUTLIERS *****')
        if variabili_da_droppare:
            df = df.drop(variabili_da_droppare, axis=1)
        for col in df.columns:
            # calcolo differenza interquartile
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1 # iqr sta per 'Differenza interquartile'
            # calcolo limiti inferiore/superiore outliers
            limite_inferiore = q1 - 1.5 * iqr
            limite_superiore = q3 + 1.5 * iqr
            # individuazione outliers
            outliers = df[(df[col] < limite_inferiore) | (df[col] > limite_superiore)]
            print(f'Nella colonna {col} sono presenti n° {len(outliers)} ({len(outliers) / len(df) * 100}%)')