import mioPrimoIDL_pb2
import mioPrimoIDL_pb2_grpc
import grpc
from concurrent import futures

class CiaoneServicerImpl(mioPrimoIDL_pb2_grpc.CiaoneServicer):
    
    def diciCiao(self, request, context):
        print(f"[SERVER] oggetto request {request}")
        text = "CIAO " + request.contenuto
        
        return mioPrimoIDL_pb2.msgRitorno(contenuto=text)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    servicer = CiaoneServicerImpl()
    
    mioPrimoIDL_pb2_grpc.add_CiaoneServicer_to_server(servicer=servicer, server=server)
    
    porto = server.add_insecure_port('0.0.0.0:0')
    
    print(f"[SERVER] listening on 0.0.0.0:{porto}")
    
    server.start()
    
    server.wait_for_termination()
    
if __name__ == "__main__":
    serve()