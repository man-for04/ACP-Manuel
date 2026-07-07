import time

from requests import Response
import requests
import stomp

class ServerListener(stomp.ConnectionListener):
    
    
    def __init__(self, conn) -> None:
        super().__init__()
        self.conn = conn
        self.create_campi = ['client', 'hotel', 'operator', 'nights', 'people', 'cost']
        self.update_campi = ['operator', 'nights', 'discount']

    
    
    def on_message(self, frame):
        msg = str(frame.body)
        if ("CREATE" in msg):
            #gestione CREATE
            #spacchettamento messaggio
            from_operator = msg.split('#')
            from_operator.pop(0)
            print(f'Ricevuto da operator CREATE: {from_operator}')
            
            to_db = {
                    'client': from_operator[0],
                    'hotel':from_operator[1],
                    'operator': from_operator[2],
                    'nights': int(from_operator[3]),
                    'people':int(from_operator[4]),
                    'cost':int(from_operator[5])
                    }
            
                
            print("Invio a DB: ")
            for x,y in to_db.items():
                print(f'{x}:{y}')
                
            
            #Invia json come richiesta Request
            r = requests.post(url='http://localhost:5000/create',json=to_db)
            try:
                r.raise_for_status()
                
            except requests.HTTPError:
                print("ERRORE in ricezione da CREATE!")
            
            conn.send(destination='/topic/response',body=r.text)
        
        
        elif('UPDATE' in msg):
            #gestione UPDATE
            #spacchettamento messaggio
            from_operator = msg.split('#')
            from_operator.pop(0)
            print(f'Ricevuto da operator UPDATE: {from_operator}')
            
            to_db = {
                    'discount':int(from_operator[0]),
                    'operator': from_operator[1],
                    'nights': int(from_operator[2])
                    }
            print("Invio a DB: ")
            for x,y in to_db.items():
                print(f'{x}:{y}')
                
            
            #TODO: Invia json come richiesta Request
            r=requests.put(url='http://localhost:5000/update', json=to_db)
            
            try:
                r.raise_for_status()
                
            except requests.HTTPError:
                print("ERRORE in ricezione da UPDATE!")
            
            conn.send(destination='/topic/response',body=r.text)
            
        else:
            print("ERRORE! Tipo di richiesta non valida in ", msg)
            conn.send(destination='/topic/response',body='ERROR')

if __name__ == "__main__":
    
    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.set_listener("", ServerListener(conn))
    conn.connect()
    conn.subscribe(destination='/topic/request', id=1, ack='auto')
    print("BookingManager avviato e in ascolto...")
    
    time.sleep(100)
    conn.disconnect()
    print("BookingManager chiuso")