import helloworld_pb2_grpc
import helloworld_pb2
import grpc
import sys


###crea generatore richieste di tipo HelloRequest
def generate_hello_requests():
    
    names = ["Gigi", "Manuel", "christian", "Ale"]
    
    for name in names:
        hello_request = helloworld_pb2.HelloRequest(name=name) #non va in confilitto, ma per sicurezza posso anche mettere nomi diversi
        yield hello_request #a differenza di return qui NON termina la funzione | Se usassi return, darebbe un errore
        print(f"Hello_request {hello_request} yield_data")

with grpc.insecure_channel("localhost:" + sys.argv[1]) as channel:
    #crea stub e fai chiamata rpc
    print(f"[CLIENT] channel: {channel} ")
    
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    
    print(f"[CLIENT]")
    res = stub.SayHello(helloworld_pb2.HelloRequest(name="GIGI")) #è la chiamata a procedura remota
    
    print(f"[CLIENT] risposta type {type(res)}")
    print(f"[CLIENT] risposta {res}")
    
    client_generator = generate_hello_requests() #qui non devo passare solo il nome, ma anche () per invocare la funzione
    
    #print(f"[CLIENT] ")... (solo il test per vedere che type di oggetto client_generator ritorna a seconda che uso yield o return)
    
    response_stream = stub.SayHello_stream(client_generator) #stream di richieste hello -> usare generatore che mi restituisca flusso di richieste
    
    for resp in response_stream:
        print(f"[CLIENT] response {resp}") #⭕se voglio stampare SOLO un campo, metti ad esempio resp.message [prova e vedi che cambia]