class Billionaire:

    def __init__(self, id = None, patrimonio_finale = None, nome_persona = None, eta = None, paese = None, citta = None,
                 fonte_reddito = None, industrie = None, paese_cittadinanza = None, organizzazione = None, self_made = None,
                 genere = None, stato = None, fascia_eta = None, codice_fascia_eta = None):
        self.id = id
        self.patrimonio_finale = patrimonio_finale
        self.nome_persona = nome_persona
        self.eta = eta
        self.paese = paese
        self.citta = citta
        self.fonte_reddito = fonte_reddito
        self.industrie = industrie
        self.paese_cittadinanza = paese_cittadinanza
        self.organizzazione = organizzazione
        self.self_made = self_made
        self.genere = genere
        self.stato = stato
        self.fascia_eta = fascia_eta
        self.codice_fascia_eta = codice_fascia_eta

    @classmethod
    def deserializzazione(cls, json):
        return cls(**json)

    def serializzazione(self):
        return self.__dict__

    def serializzazione_elenco_miliardari(self):
        return {
            "nome_persona": self.nome_persona,
            "fascia_eta": self.fascia_eta,
            "patrimonio_finale": self.patrimonio_finale,
            "paese_cittadinanza": self.paese_cittadinanza,
            "industrie": self.industrie,
            "genere": self.genere
        }

    def serializzazione_elenco_miliardari_per_paese(self):
        return {
            "nome_persona": self.nome_persona,
            "paese_cittadinanza": self.paese_cittadinanza,
            "paese": self.paese,
            "stato": self.stato,
            "citta": self.citta
        }

    def serializzazione_elenco_miliardari_u40_self_made(self):
        return {
            "nome_persona": self.nome_persona,
            "industrie": self.industrie,
            "fonte_reddito": self.fonte_reddito,
            "self_made": self.self_made,
            "fascia_eta": self.fascia_eta
        }

    def serializzazione_elenco_miliardari_per_fascia_eta(self):
        return {
            "nome_persona": self.nome_persona,
            "fascia_eta": self.fascia_eta,
            "patrimonio_finale": self.patrimonio_finale,
            "fonte_reddito": self.fonte_reddito,
            "citta": self.citta
        }