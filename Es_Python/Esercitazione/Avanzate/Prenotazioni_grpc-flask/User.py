import sys
from threading import Thread

import grpc
import random

import Laboratori_pb2
import Laboratori_pb2_grpc

def user_thread(mandaqui:Laboratori_pb2_grpc.GestioneLabStub):
    
    print("Thread client avviato!")
    
    scelta = random.randint(0,1)
    if(scelta==0):
        #book
        lab_number = random.randint(1,10)
        print(f"<-- Invio book {lab_number}")
        
        msg = Laboratori_pb2.Msg_labnumber(lab_number=lab_number)
        ret = mandaqui.book(msg)
        
        print(f'Ricevuto risposta a book: ', ret.ack)
        
    else:
        #delete
        lab_number = random.randint(1,10)
        
        print("<-- Invio richiesta delete",)
        
        msg = Laboratori_pb2.Empty()
        ret = mandaqui.delete(msg)
        
        print(f'Ricevuto risposta a delete: ', ret.lab_number)

if __name__ == "__main__":
    
    porto = sys.argv[1]
    print("Sono il client, porto = ", porto)
    
    with grpc.insecure_channel("127.0.0.1"+porto) as channel:
        
        proxy = Laboratori_pb2_grpc.GestioneLabStub(channel)
        
        threads = []
        
        for i in range(10):
            td = Thread(target=user_thread, args=(proxy, ))
            td.start()
            threads.append(td)
            
        for j in range(10):
            threads[j].join()
            print(f"Thread {j+1}/10 ritornato")