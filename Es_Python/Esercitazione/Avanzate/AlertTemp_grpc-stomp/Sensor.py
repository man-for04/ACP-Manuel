import temperature_pb2
import temperature_pb2_grpc
import grpc
import random
import sys

def generate_stream():
    """
    Metodo di utilità che dà un generator di 5 temperature int [50,100]
    """
    for _ in range(5):
        x = random.randint(50,100)
        print(f"---{x}")
        yield temperature_pb2.Richiesta_temperatura(temperatura=x)
        

if __name__=="__main__":
    #porto = input("Inserire porto a cui connettersi: ")
        
    porto = sys.argv[1]
    with(grpc.insecure_channel("localhost:"+porto)) as channel:
        print("Client attivato! porto: ", porto)
        
        proxy = temperature_pb2_grpc.GestioneStub(channel=channel)
        
        for _ in range(5):
            
            #1. invio stream
            richiesta = generate_stream()
            ris = proxy.stream_temp(richiesta)
            
            print("|-->stream inviato\n")
                
            print("Ottenuto risposta--> ", ris, "\n")
            
            #2. richiesta media
            print("Richiedo media...")
            media = proxy.get_average(temperature_pb2.Richiesta_vuota())
            print(f"Media ottenuta <{media}>")
            
    print("Client terminato!")

