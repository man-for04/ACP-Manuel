from threading import Lock, Condition

from requests import HTTPError, post

import Laptop_pb2_grpc
import Laptop_pb2
import grpc
import concurrent.futures

class miaCoda():
    def __init__(self, MAXSIZE) -> None:
        self.MAXSIZE = MAXSIZE
        self.buffer = []
        self.dim = 0
        
        #sincronizzazione
        self.lock = Lock()
        self.cv_prod = Condition(lock=self.lock)
        self.cv_cons = Condition(lock=self.lock)
        
    def is_empty(self):
        return self.dim==0
    
    def is_full(self):
        return self.dim==self.MAXSIZE
        
    def inserisci(self, elem):
        with self.lock:
            #produttore
            while self.is_full():
                #se è piena, mi metto in attesa
                self.cv_prod.wait()
            
            #sez critica
            self.buffer.append(elem)
            self.dim+=1
            print(f"Inserito {elem} in coda")
            #fine sez critica
            self.cv_cons.notify()
            
    def estrai(self):
        with self.lock:
            
            #consumatore
            while self.is_empty():
                #se è vuota, mi metto in attesa
                self.cv_cons.wait()
            
            #inizio sez critica
            elem = self.buffer.pop(0)
            self.dim-=1
            print(f"Estratto {elem} dalla coda")
            #fine sez. critica
            
            self.cv_prod.notify()
        return elem

class CompravenditaServicerImpl(Laptop_pb2_grpc.CompravenditaServicer):
    #implementare i metodi
    
    def __init__(self, queue:miaCoda) -> None:
        super().__init__()
        self.queue = queue
    
    def buy(self, request, context):
        
        print(f"--> user richiede rimozione. Rimuovo...")
        to_user = self.queue.estrai()
        
        #TODO: Richiesta a flask
        to_server = {'op':'buy',
                    'serial_number':to_user}
        
        r = post(url='http://127.0.0.1:5000/update_history', json=to_server)
        
        try:
            r.raise_for_status()
        except HTTPError:
            print("ATTENZIONE! Errore in buy")
            
        print(f'<buy> Ricevuto risposta {r.text}, {r.status_code}')
        #TODO: Ritorno
        return Laptop_pb2.msg_Laptop(serial_number=to_user)
        
    
    def sell(self, request, context):
        from_user = int(request.serial_number)
        print(f'--> ricevuto da user {from_user}. Inserisco in coda..')
        self.queue.inserisci(from_user)
        
        #TODO: Richiesta a flask
        to_server = {'op':'sell',
                    'serial_number':from_user}
        
        r = post(url='http://127.0.0.1:5000/update_history', json=to_server)
        
        try:
            r.raise_for_status()
        except HTTPError:
            print("ATTENZIONE! Errore in sell")
            
        print(f'<sell> Ricevuto risposta {r.text}, {r.status_code}')
        
        #TODO: Ritorno
        
        return Laptop_pb2.msg_ack(ack=True)
        
        
def apriServizio(queue):
    
    server = grpc.server(thread_pool=concurrent.futures.ThreadPoolExecutor(max_workers=10))
    
    servicer = CompravenditaServicerImpl(queue)
    
    Laptop_pb2_grpc.add_CompravenditaServicer_to_server(servicer, server)
    
    porto=server.add_insecure_port('0.0.0.0:0')
    print(f"Server listening on port {porto}")
    
    server.start()
    
    server.wait_for_termination()
    
if __name__ == "__main__":
    laptop_queue = miaCoda(5)
    apriServizio(laptop_queue)
    