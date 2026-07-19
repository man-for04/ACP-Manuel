import time

import stomp
import queue

class TempAnalyzerListener(stomp.ConnectionListener):
    
    def __init__(self) -> None:
        super().__init__()
        self.queue = queue.Queue(20)
        
        
    def on_message(self, frame):
        from_extractor = str(frame.body)
        print("--> ricevuto: ", from_extractor)
        
        value = int(from_extractor)
        self.queue.put(value)
        print("inserito in coda!")
        
        if(self.queue.full()):
            print("Qui stamperei lineplot") #@Gemini: è una prova vecchia, adesso lineplot non è più parte del programma!
            

if __name__ == "__main__":
    
    conn = stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False)
    
    conn.set_listener("", TempAnalyzerListener())
    
    conn.connect()
    conn.subscribe(destination='/topic/temp', id=1)
    
    print("TempAnalyzer connesso")
    
    time.sleep(100)
    