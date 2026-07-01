#crea servicer (implementatore) + creare il server e dire quale servicer servirà

##⭕Se lo faccio partire avendo modificato SOLO il client e non il server, dopo la prima ricezione inizia a dare errore!
##Se lato client ottengo errore UNIMPLEMENTED sarà un errore lato server

import helloworld_pb2
import helloworld_pb2_grpc
import grpc
from concurrent import futures #per creare threadpool exexutor da passare al server

class GreeterImpl(helloworld_pb2_grpc.GreeterServicer):  
    #se voglio aggiungere altri metodi, posso farlo"
    
    ##implementa tutit i metodi astratti
    def SayHello(self, request, context):
        
        print(f"[SERVER] request {request}")
        stringa_di_risposta = "CIAO " + request.name #vado a usare la stringa nel messaggio di risposta
        
        return helloworld_pb2_grpc.HelloReply(message=stringa_di_risposta)
    
    #⭕
    def SayHello_stream(self, requests, context):
        
        for req in requests:
            stringa_di_risposta = "CIAO" +req.name
            print("[SERVER] Sayhello_stream returning (stringa_di_risposta)")
            yield helloworld_pb2.HelloReply(stringa_di_risposta)


def serve():
    
    
    #crea il server multithread grpc
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    #crea impl
    greeter_impl = GreeterImpl()
    
    #aggiungi impl a server grpc
    helloworld_pb2_grpc.add_GreeterServicer_to_server(greeter_impl, server)
    
    
    #bind su host:port del mio server gRPC
    listening_port = server.add_insecure_port("0.0.0.0:0")
    
    ##fai partire il server e aspetta nuove richieste
    #attento a non farlo partire prima di qui, altrimenti le richieste non verranno servite da nessuno
    server.start()
    
    print(f"started gRpc server on 0.0.0.0 : {listening_port}")
    server.wait_for_termination() #resta blocccato qui in attesa di nuove richieste sul porto dato dal SO
    
if __name__ == "__main__":
    serve()