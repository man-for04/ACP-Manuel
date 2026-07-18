from flask import Flask, request
import pymongo

def get_database():
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    
    db = client['TaskDB']
    
    collection = db['RunningTasks']
    
    return collection

app = Flask(__name__,)

@app.route('/')
def index():
    print("Ciao!")
    return 'Ciao!'

@app.post('/CREATE')
def create():
    from_manager = request.get_json()
    coll = get_database()
    
    from_manager['running'] = 'yes' #aggiungo il campo
    
    coll.insert_one(from_manager)
    
    return 'ack'

@app.put('/UPDATE')
def update():
    from_manager = request.get_json()
    coll = get_database()
    
    #cerca tutti utenti specificati nella richiesta e che siano del tipo
    #Per ogni task trovato, aggiorna il valore
    #Se numero di core è negativo, setta running = no
    
    user = from_manager['user']
    type = from_manager['type']
    reduction = from_manager['reduction']
    
    red2 = -reduction
    
    coll.update_many(filter={'user':user, 'type':type} , update={"$inc": {'cores': red2}})
    
    coll.update_many(filter={'user':user, 'type':type, 'cores': {"$lt":0}}, update={"$set": {'running':'no'}}) #non è stato specificato di settare a 0 cores, quindi non lo faccio
    
    return 'ack'
    
@app.put('/DELETE')
def delete():
    from_manager = request.get_json()
    coll = get_database()
    
    #metti running=no per oGNI task di questo user
    user = from_manager['user']
    
    coll.update_many(filter={'user':user}, update={"$set": {'running':'no'}})
    
    return 'ack'


if __name__ == "__main__":
    print("Ciao sono il server")
    app.run(port=5001)