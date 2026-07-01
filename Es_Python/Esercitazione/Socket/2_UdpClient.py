import socket, sys

BUFSIZE = 4000
IP = "localhost"

def client(port : int, msg):
    csocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    print(f"Inviando messaggio {msg} a server {IP} {port}")
    csocket.sendto(msg.encode("UTF-8"), (IP, port))
    
    from_server, address = csocket.recvfrom(BUFSIZE)
    print(f'Ho ottenuto dal server: {from_server.decode("UTF-8")}')
    
    csocket.close()

if __name__ == "__main__":
    porto = int(sys.argv[1])
    text = sys.argv[2]
    client(porto, text)