#APPUNTI MIEI
# 
# voglio provare a iniettare un ritardo o corruzione su interfaccia di loopback -> vedere come la applicazione si comporta 
# (es robustezza, resilienza ecc)

#vedi foto del codice per introdurre delay

#sudo tc qdisc add dev lo root netem delay 1000ms
#sudo tc qdisc del dev lo root
#sudo tc qdisc add dev lo root netem corrupt 10%



#invece nel cas UDP (altro file-provalo) il delay ha lo stesso effetto. Ma se introduco corrupt (10%)? 
# Fallendo la checksum, non arriva nulla perchè UDP non effettua la ritrasmissione!
#Cosa mi dice? Devo intrdurre qualcosa a livello applicativo se voglio mantenere gli stessi protocolli (es. meccanismo di timeout)
#anche se rimuovo il guasto (da un terzo terminale) non cambia nulla, sta ancora aspettando il vecchio pacchetto che 
# non arriverà mai

#E' arrivato a server multithread/multiprocess

import socket
import sys
import time  # Import time module for latency measurement

def client(PORT):

    IP = 'localhost'    
    BUFFER_SIZE = 1024
    MESSAGE = "Hello, World!\n"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    start_time = time.time()  # Record the time before sending the request
    s.send(MESSAGE.encode("utf-8"))

    data = s.recv(BUFFER_SIZE)
    end_time = time.time()  # Record the time after receiving the reply

    latency = (end_time - start_time) * 1000  # Convert to milliseconds

    print(f"Received data: {data.decode('utf-8')}")
    print(f"Round-trip latency: {latency:.3f} ms")

    #s.close()

if __name__ == "__main__":
    try:
        PORT = int(sys.argv[1])  # Convert input to integer
    except (IndexError, ValueError):
        print("Please specify a valid PORT as an argument.")
        sys.exit(1)

    while True:
        client(PORT)
        time.sleep(1)