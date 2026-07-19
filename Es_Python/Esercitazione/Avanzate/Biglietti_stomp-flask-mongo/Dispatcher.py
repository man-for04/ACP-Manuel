import json
import time

from flask import Request, request
import requests
import stomp

class DispatcherListener(stomp.ConnectionListener):
    
    def __init__(self, conn:stomp.Connection) -> None:
        super().__init__()
        self.conn = conn
    
    def on_message(self, frame):
        
        print(f'\n--> {frame.body}')
        
        from_operator = json.loads(frame.body)
        try:
            operazione = from_operator['operazione']
            val = from_operator['val']
            
            if('CREATE' in operazione):
                #caso create 
                
                r = requests.post(url='http://127.0.0.1:5001/CREATE', json=val)
                
                r.raise_for_status()
                
                print("<-- Invio risposta CREATE a Operator: ", r.text)
                conn.send(destination='/topic/response', body=r.text)
                
                
            elif('UPDATE' in operazione):
                #caso update 
                r = requests.put(url='http://127.0.0.1:5001/UPDATE', json=val)
                
                r.raise_for_status()
                
                print("<-- Invio risposta UPDATE a Operator: ", r.text)
                conn.send(destination='/topic/response', body=r.text)
                
                
            elif('DELETE' in operazione):
                r = requests.delete(url='http://127.0.0.1:5001/DELETE', json=val)
                
                r.raise_for_status()
                
                print("<-- Invio risposta a Operator: ", r.text)
                conn.send(destination='/topic/response', body=r.text)
                
                
            else:
                print("ERRORE! Operazione richiesta non valida")
            
            
        except(IndexError, ValueError) as e:
            print("Errore nello spacchettamento json ", e)
        except(requests.HTTPError) as h:
            print("Errore http: ", h)

if __name__ == "__main__":
    conn = stomp.Connection([('127.0.0.1', 61613)])
    
    conn.set_listener("", DispatcherListener(conn))
    conn.connect(wait = True)
    conn.subscribe(destination='/topic/request', id=1)
    
    print("Dispatcher pronto!")
    
    while(True):
        time.sleep(1)
    