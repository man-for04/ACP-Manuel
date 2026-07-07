#deve gestire la connessione a una raccolta MongoDB per memorizzare i dati

from flask import Flask, Response, Request, request, make_response
import pymongo

def get_collection():
    conn = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = conn['DBPrenotazioni']
    collection = db['MyBookings']
    return collection

app = Flask(__name__)

@app.route("/")
def main():
    return("Benvenuti in flask")


@app.post("/create")
def create():
    """
    Permette di creare una prenotazione
    """
    collection = get_collection()
    
    data = request.get_json()
    
    if (data is not None):
        collection.insert_one(data)
        print("CREATE inserito correttamente!")
        return "ack - inserito correttamente"
    else:
        print("ERRORE! Dati inviati non validi!")
        return ('error', 400)
    
    
@app.put("/update")
def update():
    """
    Permette di aggiornare tutte le prenotazioni con vincolo (operator, notti) e occhio al negativo
    """
    collection = get_collection()
    
    data = request.get_json()
    
    if(data is not None):
        try:
            #procedo a spacchettare
            operator = str(data['operator'])
            nights = int(data['nights'])
            discount = int(data['discount'])
            
        except Exception as e:
            print("Errore in spacchettamento parametri!")
            return ("index error", 400)
        
        print(f"Ottenuto richiesta di UPDATE op:{operator}, nights:{nights}, discount:{discount}")
        
        query = collection.find(filter={'operator':operator, 'nights': {"$gte" : nights} }) #mi ritorna chi va modificatp
        
        for doc in query:
            print("--->E' stato trovato un documento modificabile! Modifico...")
            costo_vecchio = doc['cost']
            id = doc['_id']
            print("Trovato costo di: ", costo_vecchio)
            costo_nuovo = costo_vecchio-discount
            
            if costo_nuovo < 0:
                costo_nuovo=0
            
            ris = collection.update_one(filter={'_id':id},update={"$set":{'cost':costo_nuovo}})
            print(ris)
            
        print("Aggiornamento a buon fine")
        return "ack - aggiornato (o comunque non trovato nulla che rispettasse i parametri)"
    
    else:
        return ("formato json non corretto", 404)
    
    
if __name__ == "__main__":
    print("DBServer started")
    app.run(host="localhost", port=5000, debug=True)
    