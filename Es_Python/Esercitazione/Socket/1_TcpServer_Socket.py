import socket, time, threading

def gestoreSocket(s : socket.socket, risp : int):
    from_client = conn.recv(4000).decode("UTF-8")
    print(f"Messaggio ricevuto da client {addr} : {from_client}")
    
    text = "Ciao bello " + str(risp)
    to_client = text.encode("UTF-8")
    
    conn.send(to_client)
    print("Inviata risposta a client!")
    conn.close()


#scelgo adress porto
IP = '0.0.0.0'
PORT = 0

#creo socket e faccio bind
sserver = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sserver.bind((IP, PORT))

print("Socket creata!")

#metto in ascolto
sserver.listen()
info = sserver.getsockname()
address = info[0]
port = info[1]
print(f"[SERVER] socket listening on {address} and port {port}")

risp = 0
while risp<5:
    conn, addr = sserver.accept()
    
    print("Creata connessione con client, avvio thread...")
    td = threading.Thread(target=gestoreSocket, args=(conn, risp))
    td.start()
    
    risp+=1

sserver.close()
print("Server chiuso")



