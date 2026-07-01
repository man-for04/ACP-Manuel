#proxy.py
#implementa interfaccia e ne definisce la logica di chiamata a server. Porto e stringa forniti dal client

from interface import Interface
import socket

class Proxy(Interface):
    def __init__(self, port):
        self.port = port
        
    def inverti_stringa(self, data): #implementando
        csocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        csocket.connect(("localhost", self.port))
        
        print(f'{{PROXY}} connesso al server su porto {self.port}. Procedo a invio...')
        
        csocket.send(data.encode("utf-8"))
        print(f'{{PROXY}} messaggio {data} inviato a server')
        
        from_skeleton = csocket.recv(4000).decode("utf-8")
        #print(f'{{PROXY}} messaggio {from_skeleton} ricevuto dal server')
        return from_skeleton
