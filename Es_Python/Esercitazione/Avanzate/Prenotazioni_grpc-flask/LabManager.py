from concurrent.futures import ThreadPoolExecutor
from threading import Condition, Lock
import time

import grpc
import requests

import Laboratori_pb2
import Laboratori_pb2_grpc

class miaCoda():
    
    def __init__(self) -> None:
        self.buffer = []
        self.MAXSIZE = 5
        self.dim = 0
        
        self.lucchetto = Lock()
        self.cv_prod = Condition(lock=self.lucchetto)
        self.cv_cons = Condition(self.lucchetto)
        
    
    def is_empty(self):
        return  self.dim==0
    
    
    def is_full(self):
        return self.dim == self.MAXSIZE
    
    
    def add(self, elem):
        with self.lucchetto:
            
            while self.is_full():
                self.cv_prod.wait()
                
            self.buffer.append(elem)
            
            self.cv_cons.notify()
            
            
    def consuma(self):
        with self.lucchetto:
            
            while self.is_empty():
                self.cv_cons.wait()
                
            elem = self.buffer.pop(0)
            
            self.cv_prod.notify()
        
        return elem


class GestioneLabImpl(Laboratori_pb2_grpc.GestioneLabServicer):
    
    def __init__(self) -> None:
        self.lab_queue = miaCoda()
    
    def book(self, request:Laboratori_pb2.Msg_labnumber, context):
        print(".")
        from_user = int(request.lab_number)
        self.lab_queue.add(from_user)
        print("-->Ricevuto e inserito in coda (vado su flask)", from_user)
        
        #TODO: post
        
        payload = {'operation':'book',
                    'lab_number':from_user}
        
        
        r = requests.post(url="https://127.0.0.1:5000/book_history", json=payload)
        
        print("--> Ricevuto da flask: ", r.text)
        if 'ack' in r.text:
            return Laboratori_pb2.Ack(ack=True)
        else:
            return Laboratori_pb2.Ack(False)
        
    
    def delete(self, request, context):
        print(".")
        lab_number = int(self.lab_queue.consuma())
        print("<-- Letto dalla coda ", lab_number)
        
        #TODO: post
        
        payload = {'operation':'book',
                    'lab_number':lab_number}
        
        
        r = requests.post(url="https://127.0.0.1:5000/book_history", json=payload)
        
        print("--> Ricevuto da flask: ", r.text)
        
        return Laboratori_pb2.Msg_labnumber(lab_number=lab_number)
    
def serve():
    
    server = grpc.server(thread_pool=ThreadPoolExecutor(max_workers=10))
    servicer = GestioneLabImpl()
    Laboratori_pb2_grpc.add_GestioneLabServicer_to_server(servicer, server)
    
    port = server.add_insecure_port("0.0.0.0:0")
    
    server.start()
    
    print("Server listening on: ", port)
    
    server.wait_for_termination()
    
if __name__ =="__main__":
    serve()