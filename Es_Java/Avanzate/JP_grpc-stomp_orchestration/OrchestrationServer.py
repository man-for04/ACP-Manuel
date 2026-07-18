from concurrent.futures import ThreadPoolExecutor

import Orchestration_pb2
import Orchestration_pb2_grpc

import grpc
import stomp

class OrchestrationImpl(Orchestration_pb2_grpc.OrchestrationServicer):
    
    def __init__(self) -> None:
        self.conn = stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False)
        self.conn.connect()
    
    def orchestrate(self, request_iterator, context):
        
        print("ricevuto")
        
        ok = 'OK' #resta True se è tutto cpu/gpu , settato a False altrimenti
        
        for x in request_iterator:
            tipo = x.tipo
            task = x.task
            print(f"\n-->Ricevuto ({x+1}/4) {tipo}, {task}")
            
            if('GPU-based' in tipo):
                self.conn.send(destination='/topic/GPU', body=task)
            elif('CPU-based' in tipo):
                self.conn.send('/topic/CPU', body=task)
            else:
                ok = 'WARNING'
                
        print('<-- Invio risposta a client: ', ok)
        return Orchestration_pb2.msg_res(ritorno=ok)
    
if __name__ == "__main__":
    
    server = grpc.server(thread_pool=ThreadPoolExecutor(max_workers=10))
    servicer = OrchestrationImpl()
    
    
    Orchestration_pb2_grpc.add_OrchestrationServicer_to_server(servicer, server)
    
    porto = server.add_insecure_port("0.0.0.0:0")
    print("Server listening on: ", porto)
    
    server.start()
    
    server.wait_for_termination()