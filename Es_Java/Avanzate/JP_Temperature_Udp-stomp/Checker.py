from math import inf
import time

import stomp


valori_mid = []
valori_high = []
valori_low = []

class LowListener(stomp.ConnectionListener):
    
    def on_message(self, frame):
        msg = str(frame.body)
        print("--> low: "+msg)
        
        if('LOW' in msg):
            
            valore = float(msg.split('-')[0])
            valori_low.append(valore)
            
class MidListener(stomp.ConnectionListener):
    
    def on_message(self, frame):
        msg = str(frame.body)
        print("--> mid: "+msg)
        
        if('MID' in msg):
            
            valore = float(msg.split('-')[0])
            valori_mid.append(valore)
            
class HighListener(stomp.ConnectionListener):
    
    def __init__(self, out) -> None:
        super().__init__()
        self.out = out
    
    def on_message(self, frame):
        msg = str(frame.body)
        print("--> high: "+msg)
        out.write(msg)
        
        if('HIGH' in msg):
            
            valore = float(msg.split('-')[0])
            valori_high.append(valore)
            
    

def calcola(valori:list):
    
    minimo = +inf
    massimo = -inf
    media = 0
    conta = 0
    
    for x in valori:
        
        if x>massimo:
            massimo=x
        if x<minimo:
            minimo = x
        
        media += x
        conta+=1
        
    if conta == 0:
        media=0
    else:
        media = media/conta
        
    return minimo, massimo, media
    

if __name__ == "__main__":
    conn_low = stomp.Connection([('127.0.0.1', 61613)])
    conn_mid = stomp.Connection([('127.0.0.1', 61613)])
    conn_high = stomp.Connection([('127.0.0.1', 61613)])
    
    
    conn_low.set_listener("", LowListener())
    conn_low.connect()
    conn_low.subscribe(destination="/queue/low", id = 1)
    
    conn_mid.set_listener("", MidListener())
    conn_mid.connect()
    conn_mid.subscribe(destination="/queue/mid", id = 1)
    
    with open('error.txt', 'a') as out:
        
        conn_high.set_listener("", HighListener(out))
        conn_high.connect()
        conn_high.subscribe(destination="/queue/high", id = 1)
        time.sleep(60)
        
    minimo, massimo, media  = calcola(valori_low)
    print(f"\nLOW --- max:{massimo}, min:{minimo}, media:{media}")
    
    minimo, massimo, media  = calcola(valori_mid)
    print(f"\nMID --- max:{massimo}, min:{minimo}, media:{media}")
    
    minimo, massimo, media  = calcola(valori_high)
    print(f"\nHIGH --- max:{massimo}, min:{minimo}, media:{media}")
    
    conn_high.disconnect()
    conn_low.disconnect()
    conn_mid.disconnect()