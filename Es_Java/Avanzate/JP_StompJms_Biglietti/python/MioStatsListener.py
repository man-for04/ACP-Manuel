from multiprocessing import Process, Queue, Lock
from pdb import run
from miaCoda import miaCoda


import stomp

def statsProcess(queue:Queue, lock):
    #TODO: svuota la coda
    print("===Prelevo dalla coda")
    
    contenuto_queue=[]
    
    with lock:
        while(not queue.empty()):
            contenuto_queue.append(queue.get())
    
    #TODO: costruisci dizionario
    
    diz = {}
    diz['Jovanotti'] = 0
    diz['Ligabue'] = 0
    diz['Negramaro'] = 0
    
    for _ in contenuto_queue:
        if("Jovanotti" in _):
            diz['Jovanotti'] += 1
        elif("Ligabue" in _):
            diz['Ligabue'] += 1
        elif("Negramaro" in _):
            diz['Negramaro'] += 1
    
    print("<-- Scrivo su file... ", diz)
    
    with open("stats.txt", 'a') as file:
        file.write('\n\n')
        for key, value in diz.items():
            print(f"<--SCRIVO {key},{value}")
            file.write(f'\n-->{key}:{value}')
    
    
class MioStatsListener(stomp.ConnectionListener):
    
    def __init__(self, queue, lock) -> None:
        super().__init__()
        self.queue=queue
        self.lock=lock
    
    def on_message(self, frame):
        from_manager = str(frame.body)
        print("--> <statsProcess> ricevuto: ", from_manager)
        if("Sold" in from_manager):
            p = Process(target=statsProcess, args=(self.queue, self.lock))
            p.start()
        else:
            print("\n\nERRORE Ricevuto su stats senza 'stats'\n\n")
        print("statsProcess finito")
