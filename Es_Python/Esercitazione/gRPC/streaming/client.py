import grpc, sys
import mioStreaming_pb2, mioStreaming_pb2_grpc

def generaInput():
    ingressi = [2,4,5,1]
    for x in ingressi:
        yield mioStreaming_pb2.msgRichiesta(input=x)
        print(f"Sto scrivendo valore {x}")


if __name__ == "__main__":
    with(grpc.insecure_channel("localhost:" + sys.argv[1])) as channel:
        
        proxy = mioStreaming_pb2_grpc.FibonacciStub(channel=channel)
        
        richiesta = generaInput()
        
        resp = proxy.generaFibonacci(richiesta)
        print(f'Ho ottenuto risposta: {resp}')
        
        print("\nRIsultati ottenuti dal client:\n")
        for ris in resp:
            print(ris)
