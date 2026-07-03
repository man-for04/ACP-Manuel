#Controller.py
#flask web application
from gc import collect

from flask import Flask, request
import pymongo

def get_database():
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = client['dbSensori']
    return db



app = Flask(__name__)
@app.route("/")
def hello():
    
    return("Benvenuto su flask!")


@app.post("/sensor")
def registra_sensore():
    db = get_database()  #rif a database dbSensori
    collection = db['sensors']
    
    json = request.get_json()
    
    try:
        collection.insert_one(json)
    except Exception as e:
        print("Qualcosa è andato storto! ", str(e))
        return {"result":"failed to add sensor"}
    else:
        print("Aggiunta completata con successo!")
        return {"result":"success"}


@app.post("/data/<data_type>")
def invia_misurazione(data_type):
    db = get_database()
    json = request.get_json()
    if(data_type=='temp'):
        collection = db['temp_data']
        try:
            collection.insert_one(json)
        except Exception as e:
            print("<temp> qualcosa è andato storto! ", str(e))
            return {"result":"failed to add temp data"}
        else:
            print("<temp> Aggiunta completata con successo!")
            return {"result":"success"}
        
    elif (data_type=='press'):
        collection = db['press_data']
        try:
            collection.insert_one(json)
        except Exception as e:
            print("<press> qualcosa è andato storto! ", str(e))
            return {"result":"failed to add press data"}
        else:
            print("<press> Aggiunta completata con successo!")
            return {"result":"success"}
    else:
        print("Si è inserito un data_type non previsto!")
        return {"result":"failed due to invalid data_type"}


if __name__=="__main__":
    app.run(debug=True)