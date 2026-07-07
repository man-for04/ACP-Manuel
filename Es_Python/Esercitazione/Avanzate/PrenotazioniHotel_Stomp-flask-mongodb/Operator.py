from ctypes import sizeof
from threading import Thread, current_thread
import random
import time

import stomp

elenco_clienti = ['manuel', 'alessandro', 'christian', 'roberta', 'gianmaria', 'giovanni']
elenco_hotel = ['hotelNapoli', 'hotelGraz', 'ostelloCopenhagen', 'bbStoccolma']

class MioListener(stomp.ConnectionListener):
    
    def on_message(self, frame):
        msg = frame.body
        print(f"<Listener> Ricevuto risposta {msg}")


def doCreate(operator):
    #generare richiesta create
    
    #setup stomp
    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.connect()
    print(f"{current_thread().name} in ascolto. Creo richiesta CREATE...")
    
    
    #produzione
    client = elenco_clienti[random.randint(0,len(elenco_clienti)-1)]
    hotel = elenco_hotel[random.randint(0, len(elenco_hotel)-1)]
    nights = random.randint(1,14)
    people = random.randint(1,4)
    cost = random.randint(50,3000)
    
    richiesta : str = f'CREATE#{client}#{hotel}#{operator}#{nights}#{people}#{cost}'
    print(f"Sto inviando richiesta: {richiesta}")
    
    conn.send(destination='/topic/request', body=richiesta)
    conn.disconnect()

def doUpdate(operator):
    #generare richiesta update
    
    #setup stomp
    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.connect()
    print(f"{current_thread().name} in ascolto. Creo richiesta UPDATE...")
    
    
    #produzione
    
    nights = random.randint(1,14)
    discount = random.randint(50,3000)
    
    richiesta : str = f'UPDATE#{discount}#{operator}#{nights}'
    print(f"Sto inviando richiesta: {richiesta}")
    
    conn.send(destination='/topic/request', body=richiesta)
    conn.disconnect()


if __name__ == "__main__":
    print("Operator avviato")
    
    threads = []
    
    operators_CREATE = []
    operators_UPDATE = []
    
    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.set_listener("", MioListener())
    conn.connect()
    conn.subscribe(destination='/topic/response', id=1, ack='auto')
    
    for i in range(4):
        operator = input("Inserire username dell'operatore CREATE: ")
        operators_CREATE.append(operator)
    
    for i in range(2):
        operator = input("Inserire username dell'operatore UPDATE: ")
        operators_UPDATE.append(operator)
    
    for i in range(4):
        #avvio 4 thread CREATE
        
        td = Thread(target=doCreate, args=(operators_CREATE[i],))
        td.start()
        threads.append(td)
        
    for i in range(2):
        #avvio 2 thread UPDATE
        td = Thread(target=doUpdate, args=(operators_UPDATE[i],))
        td.start()
        threads.append(td)
        
    for t in threads:
        t.join()
        print("Thread ritornato")
        
    time.sleep(10)
    print("Operator terminato")
    conn.disconnect()