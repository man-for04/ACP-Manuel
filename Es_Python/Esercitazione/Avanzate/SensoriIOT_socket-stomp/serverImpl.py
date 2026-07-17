from multiprocessing import Queue
from threading import Thread

from IBalancer import IBalancer

def produttore(queue:Queue, tipo, domain, endpoint):
    
    to_queue = f'{tipo}https://{domain}{endpoint}'
    print("Inserisco in coda... ", to_queue)
    
    queue.put(to_queue)
    
def consumatore(queue:Queue,):
    
    while(True):
        from_queue = str(queue.get())
    
        tipo = from_queue.split('https://')[0]
        to_server = from_queue.split('https://')[1]
        print("Invio al server ", to_server, ' di tipo ', tipo)
        
        #TODO: gestire stomp

class serverImpl(IBalancer):
    
    def request(self, tipo, domain, endpoint):
        
        queue = Queue(6)
        
        prod = Thread(target=produttore, args=(queue, tipo, domain, endpoint))
        prod.start()
        
        