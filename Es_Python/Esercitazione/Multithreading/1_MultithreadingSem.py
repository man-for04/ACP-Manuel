#fatto a partire da scheletro prodotto

### ESERCIZIO: Multithreading Produttore/Consumatore
# Produttore: implementato tramite funzione target (Run function)
# Consumatore: implementato tramite ereditarietà (sottoclasse di threading.Thread)

import threading
from random import randint
from time import sleep

# --- COSTANTI ---
N_PRODUCERS = 10
N_CONSUMERS = 10
QUEUE_SIZE = 5

# ==========================================
# FUNZIONI DI SUPPORTO
# ==========================================

def space_is_available(queue):
    """
    Ritorna un booleano: True se la lunghezza della coda è minore di QUEUE_SIZE.
    """
    #TODO: Implementa la logica
    return not len(queue) == QUEUE_SIZE

def make_an_item_available(queue):
    """
    Produce un elemento casuale da 0 a 100 e lo aggiunge alla <queue>.
    Ritorna l'elemento prodotto.
    """
    # TODO: Implementa la logica
    item = randint(0,100)
    queue.append(item)
    print(f"[{threading.current_thread().name} prodotto {item} in coda]")
    return item

def get_an_available_item(queue: list):
    """
    Prende e rimuove (pop) il primo elemento dalla coda.
    Ritorna l'elemento rimosso.
    """
    # TODO: Implementa la logica
    item = queue.pop(0)
    print(f'[{threading.current_thread().name}] {item} rimosso dalla coda')
    return item

def an_item_available(queue):
    """
    Ritorna un booleano: True se la coda non è vuota.
    """
    # TODO: Implementa la logica
    return not len(queue) == 0


# ==========================================
# LOGICA PRODUTTORE (Callable Object)
# ==========================================

def produci(sem_prod : threading.Semaphore, sem_cons : threading.Semaphore, mutex_prod : threading.Semaphore, queue:list):
    """
    Funzione target per i thread produttori.
    Gestisce l'accesso alla coda in mutua esclusione tramite monitor (Condition).
    """
    print(f"[{threading.current_thread().name}] INIZIO PROD")
    
    sem_prod.acquire()
    
    #accedo solo se è possibile produrre
    print(f'[{threading.current_thread().name}] voglio produrre, competo con altri...')
    
    with mutex_prod:
        sleep(1)
        item = make_an_item_available(queue)
        print(f'[{threading.current_thread().name}] Ho prodotto {item} e lascio la sezione critica')
            
    sem_cons.release()
    
    print(f"[{threading.current_thread().name}] lasciata la sez critica e segnalato")


# ==========================================
# LOGICA CONSUMATORE (Sottoclasse Thread)
# ==========================================

class ConsumerThread(threading.Thread):
    
    def __init__(self, sem_cons : threading.Semaphore, sem_prod:threading.Semaphore, mutex_cons:threading.Semaphore, queue: list, name: str):
        # TODO: Inizializza la superclasse threading.Thread passando il nome
        threading.Thread.__init__(self, name=name)
        self.sem_cons = sem_cons
        self.sem_prod = sem_prod
        self.mutex_cons = mutex_cons
        self.queue = queue

    def run(self):
        print(f"[{threading.current_thread().name}] INIZIO CONS")
        
        self.sem_cons.acquire()
        print(f'[{threading.current_thread().name}] voglio consumare, competo con altri...')
        
        with self.mutex_cons:
            sleep(1)
            item = get_an_available_item(self.queue)
            print(f'[{threading.current_thread().name}] {item} consumato!')
        
        self.sem_prod.release()
            
        print(f"[{threading.current_thread().name}] lasciata sez critica e segnalato")


# ==========================================
# MAIN
# ==========================================

def main():
    print("Inizio main\n")
    
    # TODO: 1. Definisci la risorsa condivisa (la coda come lista vuota)
    queue = []
    
    # TODO: Crea semafori --> Ricorda che ne servono 4
    mutex_prod = threading.Semaphore(1)
    mutex_cons = threading.Semaphore(1)
    
    sem_prod = threading.Semaphore(QUEUE_SIZE)
    sem_cons = threading.Semaphore(0)
    
    # Liste per mantenere i riferimenti ai thread
    producers = []
    consumers = []
    
    print("[MAIN] creati queue, sem, array di prod e cons. Passo a avviare thread...")

    # TODO: 4. Crea e avvia N_PRODUCERS thread usando 'produci' come target.
    for i in range(0, N_PRODUCERS):
        td = threading.Thread(name=("prod_"+str(i)), target= produci, args=(sem_prod, sem_cons, mutex_prod, queue))
        
        td.start()
        
        producers.append(td)
    # Salvati il riferimento nella lista producers.
    
    # TODO: 5. Crea e avvia N_CONSUMERS thread istanziando la classe ConsumerThread.
    # Salvati il riferimento nella lista consumers.
    for j in range(0, N_CONSUMERS):
        td = ConsumerThread(sem_cons, sem_prod,mutex_cons, queue, name=("cons_"+str(j)))
        
        td.start()
        
        consumers.append(td)

    # TODO: 6. Fai la join() di tutti i thread produttori
    for p in producers:
        p.join()
        print(f'Thread {p.name} ritornato')
    
    # TODO: 7. Fai la join() di tutti i thread consumatori
    for c in consumers:
        c.join()
        print(f'Thread {c.name} ritornato')
    
    print("\nFine main")

if __name__ == '__main__':
    main()