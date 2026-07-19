import time

import stomp
import queue

class PressAnalyzerListener(stomp.ConnectionListener):
    
    def __init__(self, out) -> None:
        super().__init__()
        self.out = out
        self.conta = 1
        
    def on_message(self, frame):
        from_extractor = str(frame.body)
        print("--> ricevuto: ", from_extractor)
        
        value = int(from_extractor)
        
        out.write(f'{self.conta} -- {value}\n') #sarebbe csv
        print("scritto")
            

if __name__ == "__main__":
    
    conn = stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False)
    
    with open('press.csv', 'w') as out: #@Gemini: anche CSV non è argomento d'esame, stessa cosa di lineplot. Lo tratto dunque come un normale file di testo
        
        conn.set_listener("", PressAnalyzerListener(out))
        
        conn.connect()
        conn.subscribe(destination='/topic/press', id=1)
        
        print("PressAnalyzer connesso")
        
        time.sleep(100)
    