import threading #o volendo anche as thread
import random, requests


supported_types = ["temp", "press"]
controller_host = "http://localhost:5000"

def sensor_run(sensor_id):
    
    data_type = supported_types[random.randint(0,1)] #per sceglierli a caso con equa probabilità
    
    sensor_spec = {
        
        "_id":sensor_id,
        "data_type": data_type
        
    }
    #saraà usato dalla post per registrarsi
    ##devo registrarmi presso il controller tramite POST /sensor
    sensor_uri = controller_host + "/sensor" #sempre meglio mettere pure lo slash, eviti di mancarlo del tutto
    response = requests.post(sensor_uri, json=sensor_spec)
    
    print(f'SENSOR {sensor_id} response on {sensor_uri}')
    """
    effettua 5 misurazioni invocando
    /data/<data_type>. Il campo data della misurazione è scelto in manierra casuale tra 1 e 50
    """

    try:
        response.raise_for_status()
    except requests.HTTPError:
        print(f"[SENSOR {sensor_id}] errore {response.status_code} risposta {response.text}")
    else:
        print(f"[SENSOR {sensor_id}] sensore {sensor_id} registrato sul controller")        

if __name__=="__main__":
    
    
    active_threads = []
    for i in range(1,6):
        
        thd = threading.Thread(target=sensor_run, args=(i, )) #posso scegliere se usare callable object o classe (che ha senso se vanno estesi particolari comportamenti)
        #devo avviare thread e aspettare che gli altri terminino
        thd.start()
        active_threads.append(thd)
        
    for t in active_threads:
        t.join()
        
    print("[SENSORS] all sensor threads are terminated... terminate")