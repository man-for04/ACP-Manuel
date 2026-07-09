
from time import sleep

import stomp
import sys

class BWListener(stomp.ConnectionListener):
    
    def __init__(self, stringa_input, scrittore) -> None:
        super().__init__()
        self.stringa_input = stringa_input
        self.scrittore = scrittore
    
    def on_message(self, frame):
        #comportamento
        from_server = str(frame.body)
        
        
        if(self.stringa_input in from_server):
            print("--> Ricevuto dal server: ", from_server)
            
            self.scrittore.write(from_server+'\n')
            self.scrittore.flush()
            print("Scritto su file\n")

        

if __name__ == "__main__":
    
    stringa_input = sys.argv[1]
    
    if(stringa_input not in ['bw', 'gs']):
        print("ERRORE! Stringa non valida")
        
        
    with open('bw.txt', 'a',) as scrittore:
        
        conn = stomp.Connection([('127.0.0.1', 61613)])
        conn.set_listener("",listener=BWListener(stringa_input, scrittore))
        
        conn.connect(wait=True)
        conn.subscribe(destination='/queue/bw',id=1, ack='auto')
        print("In attesa di messaggi...")
        
        sleep(60)
    
    print("ColorPrinter chiuso!")