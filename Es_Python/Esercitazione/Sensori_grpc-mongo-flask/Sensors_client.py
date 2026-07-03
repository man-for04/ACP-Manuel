#Sensors_client.py
import threading
import random
import requests

URL = 'http://localhost:5000'

def run(id, data_type):
    print(f"Thread {id} avviato con data_type: {data_type}")
    
    #Registrazione sensore
    payload = {"_id":id, "data_type":data_type}
    r = requests.post(url=URL+'/sensor', json=payload)
    r.raise_for_status()
    print(f'<Thread {id}> /sensor inviata! Risposta: {r.text}, {r.status_code}')
    
    #Invio misurazioni
    for _ in range(5):
        data = random.randint(1,50)
        json={
            "sensor_id":id,
            "data":data
        }
        r = requests.post(url=URL+'/data/'+str(data_type), json=json)
        r.raise_for_status()
        
        print(f"<Thread {id} invia misurazione {data}. Ottenuto: {r.text}, {r.status_code}")
        
    
    
if __name__ == "__main__":
    
    
    
    
    print("Client avviato!")
    
    threads = []
    supported_types = ['temp', 'press']
    
    for i in range(1,6):
        
        data_type = str(supported_types[random.randint(0,1)])
        td = threading.Thread(target=run, args=(i,data_type))
        threads.append(td)
        td.start()
        
    for thread in threads:
        thread.join()
        print(f"Thread terminato")
