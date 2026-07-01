#crea servicer (implementatore) + creare il server e dire quale servicer servirà
import helloworld_pb2
import helloworld_pb2_grpc
import grpc #serve solo a creare server (non implementatore del servizio)
from concurrent import futures #per creare threadpool exexutor da passare al server

### Server = 2 passaggi:
### A) Implementare l'interfaccia del servizio dalla sua definizione (rpcall)
class GreeterImpl(helloworld_pb2_grpc.GreeterServicer):  
    #se voglio aggiungere altri metodi, posso farlo"
    
    ##implementa tutit i metodi astratti
    def SayHello(self, request, context):
        
        print(f"[SERVER] request {request}")
        stringa_di_risposta = "CIAO " + request.name #vado a usare la stringa nel messaggio di risposta, name è il campo definito da me
        print("[SERVER] Preparato stringa di risposta e procedo con invio...")
        
        return helloworld_pb2_grpc.HelloReply(message=stringa_di_risposta)

### B) Creare ed eseguire un server gRPC per accogliere richieste dei client e inviarle all'implementazione del servizio
def serve():
    
    # 1) crea il server multithread grpc
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # 2) crea implementatore del servizio (istanza della classe appena definita)
    greeter_impl = GreeterImpl()
    
    #aggiungi impl a server grpc
    helloworld_pb2_grpc.add_GreeterServicer_to_server(greeter_impl, server)
    
    
    #bind su host:port del mio server gRPC
    listening_port = server.add_insecure_port("0.0.0.0:0") #ritorna il porto di ascolto
    
    ##fai partire il server e aspetta nuove richieste
    #attento a non farlo partire prima di qui, altrimenti le richieste non verranno servite da nessuno
    server.start()
    
    print(f"started gRpc server on 0.0.0.0 : {listening_port}")
    server.wait_for_termination() #resta blocccato qui in attesa di nuove richieste sul porto dato dal SO
    
if __name__ == "__main__":
    serve()