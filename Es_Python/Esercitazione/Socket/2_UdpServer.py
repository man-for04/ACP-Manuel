import socket, threading

def gestoreSocket(conn : socket.socket, from_client, address):
    from_client = from_client.decode("UTF-8")
    print(f"Ricevuto dal client <{address}>: '{from_client}'")
    to_client = (from_client[::-1]).encode("UTF-8")
    
    conn.sendto(to_client, address)



if __name__ == "__main__":
    
    IP = "0.0.0.0"
    PORT = 0
    BUFSIZE = 4000
    
    ssocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    ssocket.bind((IP, PORT))
    
    info = ssocket.getsockname()
    print(f"Avvio server su {info[0]}, port: {info[1]}")
    
    serviti = 0
    while serviti < 5:
        
        print("In attesa di messaggio da client...")
        text, address = ssocket.recvfrom(BUFSIZE)
    
        td = threading.Thread(target=gestoreSocket, args=(ssocket, text, address))
        td.start()
        
        serviti+=1
        
        
    ssocket.close()
