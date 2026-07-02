import grpc
import mioIDL_pb2_grpc
import mioIDL_pb2
import concurrent.futures

class sommaServicerImpl(mioIDL_pb2_grpc.sommaServicer):
    def somma2numeri(self, request, context):
        x = request.operando1
        y = request.operando2
        z=x+y
        return mioIDL_pb2.msgRisposta(risultato=z)
    
def run_server():
    server = grpc.server(thread_pool=concurrent.futures.ThreadPoolExecutor(max_workers=10))
    servicer = sommaServicerImpl()
    
    mioIDL_pb2_grpc.add_sommaServicer_to_server(servicer, server)
    
    porto = server.add_insecure_port('0.0.0.0:0')
    
    print(f"Server listening on port {porto}")
    
    server.start()
    server.wait_for_termination()
    
if __name__=="__main__":
    run_server()
    