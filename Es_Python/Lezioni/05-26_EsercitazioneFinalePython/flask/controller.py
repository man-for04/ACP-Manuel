from flask import Flask, request
from pymongo import MongoClient


controller = Flask(__name__)

def get_database():
    
    mongo_client = MongoClient("localhost", 27017) #prova a non mettere parametri, IN TEORIA dovrebbe andare bene lo stesso (default)
    return mongo_client["sensor_data"] #creo il db che si chiama così e lo ritorno al chiamante
    

#@controller.route(methods=["POST"], "/sensor") <-- posso mettere anche questo, ma è più scomodo
@controller.post("/sensor")
def add_sensor(): #è una view function che devo decorare con post e devo specificare il nome della uri (rest api), NON E' add il nome 
    
    db=get_database()
    
    print(f"[CONTROLLER] ricevuta richiesta {request}")
    body = request.get_json()
    print(f"[CONTROLLER] body {body}")
    
    #ottenuta la richiesta http e body,
    sensors_collection = db["sensors"] #prendere o creare la collection sensors_database dal db
    
    
    try: #insert può andare male per qualche motivo
        sensors_collection.insert_one(body) #documento deve essere json-like -> se già lo ho, meglio usarlo subito!
    except Exception as e:
        print("[CONTROLLER] qualacosa è andato storto nella insert_one")
        return ({"result" : "failed due to " + str(e)}, 500)
    else: 
        print("[CONTROLLER] tutto ok!")
        return {"result":"success"}
    
    
    #ricorda che in flask tutte le rotte devono restituire qualcosa al client, non puoi fermarti qui



if __name__ == "__main__":
    
    controller.run(host = "localhost", port = 5000, debug = True) #il server è multithread