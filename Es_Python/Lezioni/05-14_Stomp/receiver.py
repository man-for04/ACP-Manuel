#è il caso di semplice prodcons su coda
import stomp
import time

class MyListener(stomp.ConnectionListener): #obbligatorio per il receiver ridefinire il metodo on_message()
    
    def __init__(self, conn):
        self.conn=conn
        
    def on_message(self, frame):
        print("msg ricevuto")
        print('text: "%s"' %frame.body) #contenuto del messaggio
        print('headers:  "%s"' %frame.headers) #diversi campi, es lunghezza del messaggio, expires (vedremo), destination (importante), id della subscription, priority, timestamp
        print('cmd: "%s"' %frame.cmd)#



if __name__ == "__main__":
    conn = stomp.Connection([("127.0.0.1", 61613)])
    
    #devo specificare listener e sottoscrivere
    conn.set_listener("", MyListener(conn))
    
    ##vedi la parte di avvio del broker se non va (dopo 1.10.00) + il sito activeMQ su cui va a controllare qualcosa
    
    conn.connect(wait=True) #per attenedere che la connessione sia completata
    
    conn.subscribe("/topic/miacoda", id="1", ack="auto")
    
    time.sleep(60)
    
    conn.disconnect()
    
    #posso mandare quante volte voglio la send, verrà consumata ogni volta appena un recivotore farà lì la subscribe
    #non c'è un check da parte del broker su che nome ho messo al "tipo" di coda (miacoda) -> se uso una tipologia differente non mi arriverà mai niente
    