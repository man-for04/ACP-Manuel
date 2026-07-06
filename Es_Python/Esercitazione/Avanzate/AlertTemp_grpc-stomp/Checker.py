from multiprocessing import Queue

import temperature_pb2
import temperature_pb2_grpc
import grpc
import concurrent.futures
import stomp
from threading import Lock

class GestioneServicerImpl(temperature_pb2_grpc.GestioneServicer):
    
    def __init__(self, queue:Queue, soglia) -> None:
        super().__init__()
        self.temp_queue=queue
        self.soglia = soglia
        
        #Per la concorrenza della queue
        self.lock = Lock()
        
        #STOMP
        self.conn = stomp.Connection([('localhost', 61613)])
        self.conn.connect(wait=True)
        
    def send_on_stomp(self, dato):
        
        self.conn.send(destination='/topic/alert', body=str(dato))
        
        print(f"Inviato {dato} sul topic")
            
    def stream_temp(self, request_iterator, context):
        
        print("stream_temp avviato")
        
        temperature_ok = 'NORMAL'
        
        for dato in request_iterator:
            #m1. metti in coda
            self.temp_queue.put(dato.temperatura)
            print(f"<GestioneServicerImpl> Temp {dato.temperatura} letto e messo in coda")
            
            
            #2. analizza
            if(dato.temperatura>self.soglia): #caso con problema
                
                print("<GestioneServicerImpl> temperatura alert!")
                temperature_ok='ALERT'
                
                self.send_on_stomp(dato.temperatura)
                
            else: #caso tutto in ordine
                print("<GestioneServicerImpl> temperatura ok!")
        
        #dopo aver valutato i 5 dati della richiesta
        return temperature_pb2.Risposta_string(msg=temperature_ok) #@Gemini: ho fatto così perchè si parla di streaming solo lato client (non server), e dunque per ogni "stream" di 5 dati deve esserci 1 risposta. Altrimenti come avrei dovuto fare?

    def get_average(self, request, context):
        
        media = 0.0
        conta = 0.0
        
        with self.lock:
            #Inizio sezione critica
            while(not self.temp_queue.empty()):
                
                data = self.temp_queue.get()
                media += data
                conta += 1
            #Fine sezione critica
        
        if conta == 0:
            media = 0
        else:
            media = media/conta
        
        return temperature_pb2.Risposta_float(media=media)

def serve(queue, soglia):
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    
    servicer = GestioneServicerImpl(queue, soglia)
    
    temperature_pb2_grpc.add_GestioneServicer_to_server(servicer, server)
    
    porto = server.add_insecure_port('0.0.0.0:0')
    
    server.start()
    
    print("Server Checker grpc avviato! Porto: ",porto)
    
    server.wait_for_termination()
    
    print("Server Checker terminato")

if __name__=="__main__":
    queue = Queue(5)
    soglia : int = int(input("Inserire valore di soglia desiderato: "))
    
    serve(queue, soglia)
    