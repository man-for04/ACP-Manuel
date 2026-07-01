#NEI FATTI IMPLEMENTA SOLO IL MECCANISMO DI COMUNICAZIONE E INOLTRO DELLE RICHIESTE (la prima metà del proxy-skeleton)

from interface import Subject
import socket

class Proxy(Subject): #anche lui implementa l'interfaccia (+ il proprio costruttore)
    """
    Proxy lato client --
    Permette di delegare (via socket) il metodo
    """
    
    def __init__(self, port):
        self.port=port
        
    
    def inverti_stringa(self, data):
        """
        istanza socket e invia la stringa codificata da invertire
        Ritorna poi la stringa ricevuta dal server
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost", self.port))
        print('{PROXY} connesso al server ', s)
        
        s.send(data.encode("utf-8"))
        
        ret = s.recv(1024)
        
        s.close()
        return ret