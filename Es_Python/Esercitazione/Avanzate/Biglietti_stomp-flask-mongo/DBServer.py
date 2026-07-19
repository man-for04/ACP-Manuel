from flask import Flask, request
import pymongo

def get_collection():
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = client['DBEventi']
    collection = db['Prenotazioni']
    
    return collection

app = Flask(__name__)
@app.route('/')
def hello():
    print("Ciao!")
    return 'ciao'

@app.post('/CREATE')
def create():
    mycoll = get_collection()
    
    val = request.get_json()
    r = mycoll.insert_one(val)
    
    return f'ack: {r.inserted_id}'

@app.put('/UPDATE')
def update():
    mycoll = get_collection()
    
    val = request.get_json()
    tipologia = val['tipologia']
    email = val['email']
    identificativo_evento = val['identificativo_evento']
    
    #cerca ordini di mail e identificativo_evento, setta tipologia a tipologia
    r = mycoll.update_many(filter={"email":email, "identificativo_evento":identificativo_evento}, update={'$set' : {'tipologia':tipologia}})
    
    return f'modificati: {r.modified_count}'

@app.delete('/DELETE')
def delete():
    mycoll = get_collection()
    val = request.get_json()
    
    tipologia = val['tipologia']
    data = val['data']
    #cancella biglietti di tipologia specificata e con data successiva a quella della richiesta
    
    r = mycoll.delete_many(filter={"tipologia":tipologia, "data":{'$gt':data}})
    
    return f'rimossi: {r.deleted_count}'


if __name__ == "__main__":
    app.run(debug=True, port=5001)
    print("Ciao flask")