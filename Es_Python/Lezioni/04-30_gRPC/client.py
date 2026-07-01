import helloworld_pb2_grpc
import helloworld_pb2
import grpc
import sys

#creaimo un canale verso il server
with grpc.insecure_channel("localhost:" + sys.argv[1]) as channel:
    #crea stub e fai chiamata rpc
    print(f"[CLIENT] channel: {channel} ")
    
    #creo stub
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    
    print(f"[CLIENT]")
    res = stub.SayHello(helloworld_pb2.HelloRequest(name="GIGI")) #è la chiamata a procedura remota
    
    print(f"[CLIENT] risposta type {type(res)}")
    print(f"[CLIENT] risposta {res}")