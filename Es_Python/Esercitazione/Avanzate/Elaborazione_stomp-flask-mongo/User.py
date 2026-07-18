import sys
from threading import Thread
import time

import stomp
import random

types = ['cpu-bound', 'gpu-bound']

#è UN CLIENT stomp che invia richieste di 3 tipi du topic request

class MioListener(stomp.ConnectionListener):
    
    def on_message(self, frame):
        print("--> Ricevuto risposta: ", frame.body)

def thread_create(conn:stomp.Connection, utente):
    
    user = utente
    task = 'taskn'
    type = types[random.randint(0,1)]
    cores = random.randint(1,8)
    
    to_manager = f'CREATE#{user}#{task}#{type}#{cores}'
    print("<-- Invio: ", to_manager)
    
    conn.send(destination='/topic/request', body=to_manager)
    
    time.sleep(5)
    
    
    
def thread_update(conn:stomp.Connection, utente):
    
    reduction = random.randint(1,4)
    type = types[random.randint(0,1)]
    user = utente
    
    to_manager = f'UPDATE#{reduction}#{type}#{user}'
    print("<-- Invio: ", to_manager)
    
    conn.send(destination='/topic/request', body=to_manager)
    
    time.sleep(5)
    
    
def thread_delete(conn:stomp.Connection, utente):
    
    user = utente
    
    to_manager = f'DELETE#{user}'
    print("<-- Invio: ", to_manager)
    
    conn.send(destination='/topic/request', body=to_manager)
    
    time.sleep(5)
    

if __name__ == "__main__":
    
    nome = sys.argv[1]
    
    
    conn = stomp.Connection([('127.0.0.1', 61613)])
    
    conn.set_listener("", MioListener())
    conn.connect(wait=True)
    
    conn.subscribe(destination='/topic/response', id=1)
    
    #avvio thread
    print("Sono user! Benvenuto ", nome)
    threads = []
    
    for i in range(4):
        td = Thread(target=thread_create, args=(conn, nome))
        td.start()
        threads.append(td)
        
    for i in range(2):
        td = Thread(target=thread_update, args=(conn, nome))
        td.start()
        threads.append(td)
        
    td = Thread(target=thread_delete, args=(conn, nome))
    td.start()
    threads.append(td)
    
    for j in range(7):
        threads[j].join()
        print(f"Thread {j+1}/7 ritornato")
    
    
    conn.disconnect()
    
    