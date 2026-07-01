#UGUALE PER EREDITARIETA' O DELEGA
from interface import Subject
import socket

class Proxy(Subject):
    
    def __init__(self, port):
        self.port=port
        
    
    def inverti_stringa(self, data):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost", self.port))
        print('{PROXY} connesso al server ', s)
        
        s.send(data.encode("utf-8"))
        
        ret = s.recv(1024)
        
        s.close()
        return ret