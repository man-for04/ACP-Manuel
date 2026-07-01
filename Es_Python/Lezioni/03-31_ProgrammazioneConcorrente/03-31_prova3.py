#Esempio SENZA threading.local

import threading
import time


data ={} #globale a ogni thread

def worker(name, value):
    global data
    data['user'] = value #race condition
    time.sleep(1)
    print(f"{name} vede user =", data['user'])

threads = [threading.Thread(target=worker, args=("T1", "Alice")), threading.Thread(target=worker, args=("T2", "Bob")),] #creo 2 thread: mi dovrebbero memorizzare rispettivamente Alice e Bob

for t in threads:
        t.start()

for t in threads:
        t.join()