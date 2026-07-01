import mioPrimoIDL_pb2
import mioPrimoIDL_pb2_grpc
import grpc, sys


if __name__ == "__main__":
    
    with grpc.insecure_channel("localhost:" + sys.argv[1]) as channel:
        
        print(f"[CLIENT] Eccomi, channel: {channel}")
        proxy = mioPrimoIDL_pb2_grpc.CiaoneStub(channel)
        
        msg = mioPrimoIDL_pb2.msgInvio(contenuto="Mario")
        
        risposta = proxy.diciCiao(msg)
        
        print(f"[CLIENT] ho ricevuto risposta {risposta}")
        