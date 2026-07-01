### multithreading prod/cons
#--> ho deciso arbitrariamente di implementare produttore con Run function, consumatore con ridefinizione della classe

import threading  #svolgo il tutto con THREAD
from random import randint

#implemento la logica di produzione

N_PRODUCERS = 10
N_CONSUMERS = 10
QUEUE_SIZE = 5



def space_is_available(queue):
    return not len(queue) == QUEUE_SIZE #quanti elementi ho inserito in lista unbounded

def make_an_item_available(queue):
    """
    Produce un elemento casuale da 0 a 100 
    e lo aggiunge alla <queue> passata per parametro.
    Infine ritorna l'elemento prodotto
    """
    item = randint(0,100)
    queue.append(item)

    return item

#run function del 🏭 produttore
def produci(prod_cv:threading.Condition, cons_cv:threading.Condition, queue):
    print("INIZIO PROD")
    """
    Ingresso: varcond Prod + varcond Cons + coda
    va a prendere argomenti che gli ho passato
    """

    ###entro nel monitor, mi metto in attesa (ev) sulla var cond per la produzione, non posso produrre una volta segnalato sulle varcond, produco
    with prod_cv: ###lock.acquire()
        ###controlla predicato sulla prod
        while not space_is_available(queue): ###len ha raggiunto il limite
            print("[PROD] mi metto in attesa")
            prod_cv.wait()   ## NON METTERE acquire, vado a ri-richiedere il lock (l'ho già fatta interna a with)

        ### produci
        item = make_an_item_available(queue) #ritorna l'el prodotto
        print("elemento prodotto= ", item)

        ###segnalo eventuali cons
        #non fare cons_cv.release()!! 
        cons_cv.notify()
        
    ###esco dal monitor
    print("PROD lasciato il monitor")

def get_an_available_item(queue):
    """
    Prendo l'elemento dalla coda
    """
    return queue.pop(0)

def an_item_available(queue):
    return not (len(queue) == 0)


#ho deciso arbitrariamente di gestire con questa modalità il consumatore
class ConsumerThread(threading.Thread):

    def __init__(self, prod_cv, cons_cv, queue, name):

        #passerò al consumatore le var condition
        threading.Thread.__init__(self, name=name)
        self.prod_cv = prod_cv
        self.cons_cv = cons_cv
        self.queue = queue

    def run(self):

        with self.cons_cv: #è un oggetto della classe

            while not an_item_available(self.queue): #se non c'è nulla da ritirare, mi metto in attesa
                self.cons_cv.wait()

            ###consumo

            print("el consumato. ", get_an_available_item(self.queue))

            #risveglio eventuali produttori in attesa
            self.prod_cv.notify()

def main():
    print("Inizio main\n\n")
    #definire una risorsa condivisa, multiple buffer
    queue = []
    """
    PROCEDIMENTO MENTALE
    Ricorda che coda è acceduta in mutua esclusione (blocco l'intera coda - soluzione naive)
    Posso usare semplicemente mutex (ma così non posso usare cooperazione) -> devo avere o qualche meccanismo di comunicazione
    oppure(soluzione + semplice)  vado a usare un monitor signal-and-continue
    """

    ##uso monitor, quante variabili condition vanno usate? 2 | 1 andrebbe bene? Si, blocco tutto -> però semanticamente è meglio separare i concetti
    ###var cond
    ###lock che uso per accedere al monitor
    cv_lock = threading.Lock() ###posso usare multiprocessing.Lock() ? Posso usarlo, ma mi chiederà il perchè --> cerca
    prod_cv = threading.Condition(lock=cv_lock) ### perchè non Rlock? Non ho casi in cui può servire la parte ricorsiva, inutile renderlo più oneroso del necessario! 
                                                ### Rlock è anche più pericoloso, potrebbe lockarmi più volte (non è previsto nel prodcons) e potrei non accorgermene
    cons_cv = threading.Condition(lock=cv_lock)

    """
    #IN CASO DI APPLICAZIONE MULTIPROCESS -> sostituisco threading con multiprocessing -> Funziona? NO 1)Dipende dal SO, 2) Gli oggetti sono serializzabili? Non posso usare per la condivisione un oggetto non condiviso, ho bisogno di porre la lista in una shmem o usare una queue
    queue = []
    queue = multiprocessing.Queue(QUEUE_SIZE) -> spazio di memoria condiviso tra tutti i processi, "sotto" userà un qualche tipo di shmem Posix-compliant
    """
    ### crea N consum crea N prod ->nell'esempio uno è chiamato normalmente (callable object), l'altro estendendo la classe thread (ovviamente non è necessario, l'estensione serve solo se devo es. aggiungere altri metodi ecc)

    #mantengono produttori e consumatori
    producers = []
    consumers = []

    ###start thread 
    #crea i prod con callable object
    for i in range(N_PRODUCERS):

        p_prod = threading.Thread(target=produci, name="PROD "+str(i), args=(prod_cv, cons_cv, queue)) #se non specifico name, viene usato name specifico della classe main thread

        p_prod.start()
        #creo lista di oggetti thread per mantenermi la lista di thread
        producers.append(p_prod)

    #crea i cons istanziando oggetti della classe ridefinita
    for i in range(N_CONSUMERS):

        ct = ConsumerThread(prod_cv, cons_cv, queue, name="CONS "+str(i))
        ct.start()

        consumers.append(ct)

    ###join thread
    for prod in producers:
        prod.join()


    for cons in consumers:
        cons.join()

if __name__=='__main__':
    main()