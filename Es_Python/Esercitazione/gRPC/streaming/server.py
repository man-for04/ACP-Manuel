#server che gestisce lo streaming in uscita con yield

#TODO: Implementare classe astratta
#TODO: Definire funzionamento server con ev. funzione generatrice apposita (che include lo yield invece che return)

import grpc, concurrent.futures
import mioStreaming_pb2, mioStreaming_pb2_grpc

class FibonacciServicerImpl(mioStreaming_pb2_grpc.FibonacciServicer):
    def generaFibonacci(self, request_iterator, context): #al posto di fibonacci faccio quadrato per semplicità
        for a in request_iterator:
            risp = a.input
            risp = risp**2
            yield mioStreaming_pb2.msgRisposta(output=risp)
            
def run_server():
    server = grpc.server(thread_pool=concurrent.futures.ThreadPoolExecutor(max_workers=10))
    servicer = FibonacciServicerImpl()
    
    mioStreaming_pb2_grpc.add_FibonacciServicer_to_server(servicer, server)
    
    porto = server.add_insecure_port('0.0.0.0:0')
    
    print(f"Server listening on {porto}")
    
    server.start()
    
    server.wait_for_termination()

if __name__ == "__main__":
    run_server()