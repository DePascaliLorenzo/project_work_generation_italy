from flask import Flask, request
from service.billionaire_service import BillionaireService

app = Flask(__name__)

miliardari_service = BillionaireService()

# ********** ENDPOINT **********

# endpoint elenco miliardari
# localhost:5000/miliardari/get
@app.get('/miliardari/get')
def endpoint_elenco_miliardari():
    return miliardari_service.elenco_miliardari()

# endpoint elenco miliardari per paese
# localhost:5000/miliardari/get-paesi
@app.get('/miliardari/get-paesi')
def endpoint_elenco_miliardari_per_paese():
    return miliardari_service.elenco_miliardari_per_paese()

# endpoint elenco miliardari u40 self made
# localhost:5000/miliardari/get-u40/<string:self_made>
@app.get('/miliardari/get-u40/<string:self_made>')
def endpoint_elenco_miliardari_u40_self_made_false(self_made):
    return miliardari_service.elenco_miliardari_self_made_u40(self_made)

# endpoint elenco miliardari per fascia d'età
# localhost:5000/miliardari/get-miliardari/<integer:codice_fascia_eta>
@app.get('/miliardari/get-miliardari/<int:codice_fascia_eta>')
def endpoint_elenco_miliardari_per_fascia_eta(codice_fascia_eta):
    return miliardari_service.elenco_miliardari_per_fascia_eta(codice_fascia_eta)

if __name__ == '__main__':
    app.run()


if __name__ == '__main__':
    app.run()