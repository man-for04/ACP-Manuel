import socket, time, sys

def client(port:int):
    csocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    
    csocket.connect(("localhost", port))
    print(f"Client si è connesso a server <localhost,{port}>")
    
    text = "CIAO, sono il client!"
    to_server = text.encode("UTF-8")
    print("Messaggio inviato!")
    
    csocket.send(to_server)
    
    from_server = csocket.recv(4000).decode("UTF-8")
    
    print(f"Ricevuto messaggio dal server: {from_server}")
    print("client muore")
    
    csocket.close()


if __name__ == "__main__":
    porto = int(sys.argv[1])
    client(porto)

