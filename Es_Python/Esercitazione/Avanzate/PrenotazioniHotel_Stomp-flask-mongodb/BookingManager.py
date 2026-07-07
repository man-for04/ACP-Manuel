import time

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
                
            
            #TODO: Invia json come richiesta Request
            #TODO: RIcevi e inoltra a Operator la risposta
            conn.send(destination='/topic/response',body='Ok create')
        
        
        elif('UPDATE' in msg):
            #gestione UPDATE
            #spacchettamento messaggio
            from_operator = msg.split('#')
            from_operator.pop(0)
            print(f'Ricevuto da operator CREATE: {from_operator}')
            
            to_db = {
                    'operator': from_operator[0],
                    'nights': int(from_operator[1]),
                    'discount':int(from_operator[2])
                    }
            print("Invio a DB: ")
            for x,y in to_db.items():
                print(f'{x}:{y}')
                
            
            #TODO: Invia json come richiesta Request
            #TODO: RIcevi e inoltra a Operator la risposta
            conn.send(destination='/topic/response',body='Ok update')
            
        else:
            print("ERRORE! Tipo di richiesta non valida in ", msg)
            conn.send(destination='/topic/response',body='ERROR')

if __name__ == "__main__":
    
    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.set_listener("", ServerListener(conn))
    conn.connect()
    conn.subscribe(destination='/topic/request', id=1, ack='auto')
    print("BookingManager avviato e in ascolto...")
    
    time.sleep(60)
    conn.disconnect()
    print("BookingManager chiuso")