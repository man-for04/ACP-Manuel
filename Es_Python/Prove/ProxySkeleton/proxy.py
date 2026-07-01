from serverInterface import ServerInterface
import socket

#si deve occipare della logica di connessione del client
class Proxy(ServerInterface):
    
    def __init__(self, port):
        self.port = port #ho bisogno del porto per collegarmi
        
    def inverti_stringa(self, data):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', self.port))
        
        print(f"<PROXY> connesso al server {'localhost'}, porto: {self.port}")
        
        s.send(data.encode("utf-8"))
        
        rec = s.recv(1024).decode("utf-8")
        
        s.close()
        print("<PROXY> ricevuto dato e chiuso")
        
        return rec