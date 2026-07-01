#fatto a partire da scheletro prodotto

### ESERCIZIO: Multithreading Produttore/Consumatore
# Produttore: implementato tramite funzione target (Run function)
# Consumatore: implementato tramite ereditarietà (sottoclasse di threading.Thread)

import threading
from random import randint

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

def produci(prod_cv: threading.Condition, cons_cv: threading.Condition, queue: list):
    """
    Funzione target per i thread produttori.
    Gestisce l'accesso alla coda in mutua esclusione tramite monitor (Condition).
    """
    print(f"[{threading.current_thread().name}] INIZIO PROD")
    
    with prod_cv: ##corrisponde a acquire-> entro in sezione critica
        while(not space_is_available(queue)):
            print(f"[{threading.current_thread().name}] mi metto in attesa")
            prod_cv.wait()
            print(f"[{threading.current_thread().name}] mi sveglio")
    
        el = make_an_item_available(queue)
        print(f"[{threading.current_thread().name}] Prodotto elemento {el}")
        cons_cv.notify()

    # TODO: 1. Entra nel monitor usando la condition del produttore
    # TODO: 2. Controlla il predicato: finché non c'è spazio, mettiti in attesa
    # TODO: 3. Produci l'elemento (usa la funzione di supporto) e stampalo
    # TODO: 4. Segnala (notify) eventuali consumatori in attesa
    # (L'uscita dal monitor è automatica se usi il costrutto with)
    
    print(f"[{threading.current_thread().name}] lasciato il monitor")


# ==========================================
# LOGICA CONSUMATORE (Sottoclasse Thread)
# ==========================================

class ConsumerThread(threading.Thread):
    
    def __init__(self, prod_cv: threading.Condition, cons_cv: threading.Condition, queue: list, name: str):
        # TODO: Inizializza la superclasse threading.Thread passando il nome
        threading.Thread.__init__(self, name=name)
        self.prod_cv = prod_cv
        self.cons_cv = cons_cv
        self.queue = queue
        # TODO: Salva le variables condition e la coda come attributi di istanza (self)
        

    def run(self):
        # TODO: 1. Entra nel monitor usando la condition del consumatore (self.cons_cv)
        print(f"[{threading.current_thread().name}] INIZIO CONS")
        
        with self.cons_cv:
            
            while(not an_item_available(self.queue)):
                print(f"[{threading.current_thread().name}] mi metto in attesa")
                self.cons_cv.wait()
                print(f"[{threading.current_thread().name}] mi sveglio")
            # TODO: 2. Controlla il predicato: finché non ci sono elementi, mettiti in attesa
            # TODO: 3. Consuma l'elemento (usa la funzione di supporto) e stampalo
            item = get_an_available_item(self.queue)
            print(f'[{threading.current_thread().name}] {item} consumato!')
            # TODO: 4. Risveglia (notify) eventuali produttori in attesa
            self.prod_cv.notify()
            
        print(f"[{threading.current_thread().name}] lasciato il monitor")


# ==========================================
# MAIN
# ==========================================

def main():
    print("Inizio main\n")
    
    # TODO: 1. Definisci la risorsa condivisa (la coda come lista vuota)
    queue = []
    
    # TODO: 2. Crea un Lock per l'accesso in mutua esclusione
    lock = threading.Lock()
    
    
    # TODO: 3. Crea due variabili Condition (prod_cv, cons_cv) associandole allo stesso Lock
    prod_cv = threading.Condition(lock=lock)
    cons_cv = threading.Condition(lock=lock)
    
    # Liste per mantenere i riferimenti ai thread
    producers = []
    consumers = []
    
    print("[MAIN] creati queue, lock, cv, array di prod e cons. Passo a avviare thread...")

    # TODO: 4. Crea e avvia N_PRODUCERS thread usando 'produci' come target.
    for i in range(0, N_PRODUCERS):
        td = threading.Thread(name=("prod_"+str(i)), target= produci, args=(prod_cv, cons_cv, queue))
        
        td.start()
        
        producers.append(td)
    # Salvati il riferimento nella lista producers.
    
    # TODO: 5. Crea e avvia N_CONSUMERS thread istanziando la classe ConsumerThread.
    # Salvati il riferimento nella lista consumers.
    for j in range(0, N_CONSUMERS):
        td = ConsumerThread(prod_cv, cons_cv, queue, name=("cons_"+str(j)))
        
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