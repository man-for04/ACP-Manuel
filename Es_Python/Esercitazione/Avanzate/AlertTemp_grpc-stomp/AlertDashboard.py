from multiprocessing import Process

import stomp
import time

def run(frame):
    print(f"Temperatura ricevuta: {frame}°")
    with(open("./alerts.txt", 'a')) as file:
        file.write(str(frame)+'\n')
    print("Scrittura su file completata!")

class MioListener(stomp.ConnectionListener):
    def on_message(self, frame):
        
        p = Process(target=run, args=(frame.body,))
        p.start()
        


if __name__ =="__main__":
    
    with(stomp.Connection([('localhost', 61613)])) as conn:
        
        conn.connect(wait=True)
        
        conn.set_listener("", MioListener())
        
        conn.subscribe('/topic/alert', id=1, ack="auto")
        
        print("Benvenuti al dashboard!")
        
        while(True):
            time.sleep(1)