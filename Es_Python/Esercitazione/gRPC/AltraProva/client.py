import grpc, sys
import mioIDL_pb2_grpc
import mioIDL_pb2
import concurrent.futures

if __name__=="__main__":
    with(grpc.insecure_channel("localhost:"+sys.argv[1])) as channel:
        
        proxy = mioIDL_pb2_grpc.sommaStub(channel=channel)
        
        response = proxy.somma2numeri(mioIDL_pb2.msgRichiesta(operando1=int(sys.argv[2]), operando2=int(sys.argv[3])))
        
        print(f"Ho ottenuto risposta {response}")