
from threading import Thread

import Laptop_pb2
import Laptop_pb2_grpc
import grpc
import sys
from random import randint

def workerThread(proxy):
    r = randint(0,1)
    if(r==0):
        #sell
        to_manager = Laptop_pb2.msg_Laptop(serial_number=randint(1,100))
        print(f"<-- Invio a manager {to_manager.serial_number}")
        from_manager = proxy.sell(to_manager)
        print(f"--> <sell> ricevuto risposta {from_manager}")
    
    else:
        #buy
        to_manager = Laptop_pb2.msg_Void()
        print(f"<-- Invio a manager buy")
        from_manager = proxy.buy(to_manager)
        print(f"--> <sell> ricevuto risposta {from_manager}")
    

if __name__ == "__main__":
    
    porto = sys.argv[1]
    print("Porto inserito: ", porto)
    
    threads = []
    
    with grpc.insecure_channel(target="localhost:"+porto) as channel:
    
        proxy = Laptop_pb2_grpc.CompravenditaStub(channel=channel)
        
        for i in range (10):
            td = Thread(name=f'thread_{i}', target=workerThread, args=(proxy,))
            td.start()
            print(f"thread {i} avviato")
            threads.append(td)
            
        for i in range(10):
            threads[i].join()
            print(threads[i].name, "ritornato")