#Esempio CON threading.local

import threading
import time

#storage locale per thread
data = threading.local() #data è locale ad ogni thread

def worker(name, value):
    data.user = value
    time.sleep(2)
    print(f"{name} vede user=", data.user)

threads = [threading.Thread(target=worker, args=("T1", "Alice")), threading.Thread(target=worker, args=("T2", "Bob")),] #creo 2 thread: mi dovrebbero memorizzare rispettivamente Alice e Bob

for t in threads:
    t.start()

for t in threads:
    t.join()