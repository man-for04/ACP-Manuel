from ast import arg
import json
from threading import Thread
import time

import stomp
import random

tipologie = ['prato', 'prato-gold', 'curva']
identificativi = ['AER3', 'OOD1', 'IU73', 'F5RE']
emails = ['fornataro.ma@gmail.com', 'ldesi@hotmail.com', 'unina@unina.it','aaaaaa@aaa.aa']
nomi = ['Manuel', 'Roberta', 'Christian']
cognomi = ['Fornataro', 'Giovengo', 'Formicola']

class OperatorListener(stomp.ConnectionListener):
    
    def on_message(self, frame):
        print("--> RISPOSTA: ", frame.body)


def thread_create(conn : stomp.Connection):
    identificativo_evento = identificativi[random.randint(0,3)]
    intestatario = f'{nomi[random.randint(0,2)]} {cognomi[random.randint(0,2)]}'
    email = emails[random.randint(0,3)]
    tipologia = tipologie[random.randint(0,2)]
    data = int(20260719)
    numbero_biglietti = random.randint(1,4)
    
    val = {'identificativo_evento':identificativo_evento,
            'intestatario':intestatario,
            'email':email,
            'tipologia':tipologia,
            'data':data,
            'numbero_biglietti':numbero_biglietti}
    
    to_dispatcher = json.dumps({'val':val,
                                'operazione':'CREATE'})
    
    print(f"<-- [{to_dispatcher}]")
    
    conn.send(destination='/topic/request', body=to_dispatcher)
    print("inviato\n")


    
def thread_update(conn:stomp.Connection):
    tipologia = tipologie[random.randint(0,2)]
    email = emails[random.randint(0,3)]
    identificativo_evento = identificativi[random.randint(0,3)]
    
    val = {'tipologia':tipologia,
            'email':email,
            'identificativo_evento':identificativo_evento}
    
    to_dispatcher = json.dumps({'val':val,
                                'operazione':'UPDATE'})
    
    print(f"<-- [{to_dispatcher}]")
    
    conn.send(destination='/topic/request', body=to_dispatcher)
    print("inviato\n")
    

def thread_delete(conn:stomp.Connection):
    tipologia = tipologie[random.randint(0,2)]
    data = 20260101
    
    val = {'tipologia':tipologia,
            'data':data}
    
    to_dispatcher = json.dumps({'val':val,
                                'operazione':'DELETE'})
    
    print(f"<-- [{to_dispatcher}]")
    
    conn.send(destination='/topic/request', body=to_dispatcher)
    print("inviato\n")



if __name__=="__main__":
    #setup stomp
    conn = stomp.Connection(host_and_ports=[('127.0.0.1', 61613)])
    
    conn.set_listener("", OperatorListener())
    conn.connect(wait = True)
    conn.subscribe(destination='/topic/response', id=1)
    
    threads = []
    
    print("Sono operator!")
    
    for i in range(4):
        td = Thread(target=thread_create, args=(conn,))
        td.start()
        threads.append(td)
        
    for i in range(2):
        td = Thread(target=thread_update, args=(conn,))
        td.start()
        threads.append(td)
        
    td = Thread(target=thread_delete, args=(conn,))
    td.start()
    threads.append(td)
    
    time.sleep(5)
    
    
    
    for j in range(len(threads)):
        threads[j].join()
        print(f'Thread {j+1}/7 ritornato')
    