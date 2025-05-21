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