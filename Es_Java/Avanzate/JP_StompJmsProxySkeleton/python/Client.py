from time import sleep
import stomp
import random

tipi_richieste = ['deposita', 'preleva']

class ClientListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn
        
    def on_message(self, frame):
        print(f"<CLIENT> Messaggio ricevuto dal dispatcher: '{frame.body}'")

if __name__ == "__main__":
    
    conn=stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False)
    
    conn.connect(wait=True)
    
    print(f"<CLIENT> Connesso a {conn.is_connected}")
    
    #Invio N messaggi
    try:
        N = 10
        for _ in range(N):
            
            tipo_richiesta = tipi_richieste[random.randint(0,1)]
            
            id_articolo = random.randint(1,1000)
            
            msg = tipo_richiesta + "#" + str(id_articolo)
            
            print("<CLIENT> Invio mess: ", msg)
            
            conn.send('/queue/Richiesta',msg, headers={"reply-to":"/queue/Risposta"})
            
            
    except IndexError:
        print("Errore nel recupero dei parametri!")
        
        #setup di ascolto su Risposta
    conn.set_listener('', ClientListener(conn=conn))
    conn.subscribe('/queue/Risposta', id=1, ack='auto')
        
    print("In attesa di risposte...")
    
    sleep(60)

    print("Mi disconnetto!")
    conn.disconnect()
    
    