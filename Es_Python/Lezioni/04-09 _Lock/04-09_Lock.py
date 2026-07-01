import threading #permette di risolvere il nome della classe
import time
from threading import Lock

x=10

def increment(val, lock):
    """
        increment incrementerà x rispetto al valore val
        """
    global x #forzo a operare i 2 thread sullo stesso oggetto -> intero è immutabile (creerebbe un nuovo oggetto se passato come parametro)

    lock.acquire()

    local_counter = x
    local_counter += val

    time.sleep(1)

    x=local_counter

    print(f'{threading.current_thread().name} incrementa x di {val}, x: {x}') #ritorna 'identificativo' del thread

    lock.release()

l = Lock() #devo passarlo a tutti i thread

t1 = threading.Thread(target=increment, args = (5,l))
t2 = threading.Thread(target=increment, args = (10,l))

t1.start()
t2.start()

t1.join()
t2.join()

print(f'{threading.current_thread().name} valore finale di x: {x}')