import time

import requests
import stomp

class ManagerListener(stomp.ConnectionListener):
    
    def __init__(self, conn) -> None:
        super().__init__()
        
        self.conn = conn
        
    def on_message(self, frame):
        print("\n--> Ricevuto richiesta: ", frame.body)
        
        from_user = str(frame.body).split('#')
        
        
        try:
            if ('CREATE' in frame.body):
                
                user = from_user[1]
                task = from_user[2]
                type = from_user[3]
                cores = int(from_user[4])
                
                to_flask = {'user':user,
                            'task':task,
                            'type':type,
                            'cores':cores}
                
                #TODO: invia richieste
                
                r = requests.post(url='http://127.0.0.1:5001/CREATE', json=to_flask)
                
                print('--> Ricevuto da flask: ', r.text)
                
                self.conn.send(destination='/topic/response', body=r.text)
                
                
            elif('UPDATE' in frame.body):
                
                reduction = int(from_user[1])
                type = from_user[2]
                user = from_user[3]
                
                to_flask = {'reduction':reduction,
                            'type':type,
                            'user':user}
            
                r = requests.put(url='http://127.0.0.1:5001/UPDATE', json=to_flask)
                
                print('--> Ricevuto da flask: ', r.text)
                
                self.conn.send(destination='/topic/response', body=r.text)
                
                
            elif('DELETE' in frame.body):
                
                user = from_user[1]
                
                to_flask = {'user':user}
                
                r = requests.put(url='http://127.0.0.1:5001/DELETE', json=to_flask)
                
                print('--> Ricevuto da flask: ', r.text)
                
                self.conn.send(destination='/topic/response', body=r.text)
                
            else:
                print("ERRORE! Non riconosciuto!")
                conn.send(destination='/topic/response', body='error')
        except(TypeError | IndexError ) as e:
            print("Errore!")
            print(e)
            
        
if __name__ == "__main__":
    
    with (stomp.Connection([('127.0.0.1', 61613)])) as conn:
        
        conn.set_listener("", ManagerListener(conn))
        conn.connect(wait=True)
        
        conn.subscribe(destination='/topic/request', id=1)
        
        print("Connesso!")
        
        while(True):
            time.sleep(1)