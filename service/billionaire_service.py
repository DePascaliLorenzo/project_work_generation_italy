from model.billionaire import Billionaire
from repository.repository import Repository

class BillionaireService:

    def __init__(self):
        self.repository = Repository()

    def elenco_miliardari(self):
        sql = 'SELECT * from elenco_miliardari'
        ottenuto_db = self.repository.recupero_multiplo(sql)
        if isinstance(ottenuto_db, str):
            return {"codice": 500, "messaggio": ottenuto_db}, 500
        miliardari = []
        for record in ottenuto_db:
            miliardario = Billionaire(nome_persona=record[0], fascia_eta=record[1], patrimonio_finale=record[2],
                                      paese_cittadinanza=record[3], industrie=record[4], genere = record[5])
            miliardari.append(miliardario.serializzazione_elenco_miliardari())
            if isinstance(ottenuto_db, str):
                return {"codice": 500, "messaggio": ottenuto_db}, 500  # errore db
        return miliardari

    def elenco_miliardari_per_paese(self):
        sql = 'SELECT * from miliardari_paesi'
        ottenuto_db = self.repository.recupero_multiplo(sql)
        if isinstance(ottenuto_db, str):
            return {"codice": 500, "messaggio": ottenuto_db}, 500
        miliardari = []
        for record in ottenuto_db:
            miliardario = Billionaire(nome_persona=record[0], paese_cittadinanza=record[1], paese=record[2],
                                      stato=record[3], citta=record[4])
            miliardari.append(miliardario.serializzazione_elenco_miliardari_per_paese())
            if isinstance(ottenuto_db, str):
                return {"codice": 500, "messaggio": ottenuto_db}, 500  # errore db
        return miliardari

    def elenco_miliardari_self_made_u40(self, self_made):
        if self_made == 'False':
            sql = 'SELECT * from miliardari_u40self_made_false'
            ottenuto_db = self.repository.recupero_multiplo(sql)
            if isinstance(ottenuto_db, str):
                return {"codice": 500, "messaggio": ottenuto_db}, 500
            miliardari = []
            for record in ottenuto_db:
                miliardario = Billionaire(nome_persona=record[0], industrie=record[1], fonte_reddito=record[2],
                                          self_made=record[3], fascia_eta=record[4])
                miliardari.append(miliardario.serializzazione_elenco_miliardari_u40_self_made())
            return miliardari
        else:
            sql = 'SELECT * from miliardari_u40self_made_true'
            ottenuto_db = self.repository.recupero_multiplo(sql)
            if isinstance(ottenuto_db, str):
                return {"codice": 500, "messaggio": ottenuto_db}, 500
            miliardari = []
            for record in ottenuto_db:
                miliardario = Billionaire(nome_persona=record[0], industrie=record[1], fonte_reddito=record[2],
                                          self_made=record[3], fascia_eta=record[4])
                miliardari.append(miliardario.serializzazione_elenco_miliardari_u40_self_made())
            return miliardari

    def elenco_miliardari_per_fascia_eta(self, codice_fascia_eta):
        if codice_fascia_eta == 0:
            sql = 'SELECT * FROM eta_under_40'
            ottenuto_db = self.repository.recupero_multiplo(sql)
            if isinstance(ottenuto_db, str):
                return {"codice": 500, "messaggio": ottenuto_db}, 500
            miliardari = []
            for record in ottenuto_db:
                miliardario = Billionaire(nome_persona=record[0], fascia_eta=record[1], patrimonio_finale=record[2],
                                          fonte_reddito=record[3], citta=record[4])
                miliardari.append(miliardario.serializzazione_elenco_miliardari_per_fascia_eta())
            return miliardari
        elif codice_fascia_eta == 1:
            sql = 'SELECT * FROM eta_40_60'
            ottenuto_db = self.repository.recupero_multiplo(sql)
            if isinstance(ottenuto_db, str):
                return {"codice": 500, "messaggio": ottenuto_db}, 500
            miliardari = []
            for record in ottenuto_db:
                miliardario = Billionaire(nome_persona=record[0], fascia_eta=record[1], patrimonio_finale=record[2],
                                          fonte_reddito=record[3], citta=record[4])
                miliardari.append(miliardario.serializzazione_elenco_miliardari_per_fascia_eta())
            return miliardari
        else:
            sql = 'SELECT * FROM eta_over_60'
            ottenuto_db = self.repository.recupero_multiplo(sql)
            if isinstance(ottenuto_db, str):
                return {"codice": 500, "messaggio": ottenuto_db}, 500
            miliardari = []
            for record in ottenuto_db:
                miliardario = Billionaire(nome_persona=record[0], fascia_eta=record[1], patrimonio_finale=record[2],
                                          fonte_reddito=record[3], citta=record[4])
                miliardari.append(miliardario.serializzazione_elenco_miliardari_per_fascia_eta())
            return miliardari