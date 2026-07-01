#skeleton.py
from interface import Interface
import socket
from abc import ABC, abstractmethod
import threading

#--> Devo gestire la connessione con il proxy. Ricorda la questione di passare il self al thread + metodo runskeleton
def run_function(conn : socket.socket, skeleton_ref):
    from_proxy = conn.recv(4000).decode("utf-8")
    to_proxy = skeleton_ref.inverti_stringa(from_proxy)

    print(f"{{SKELETON}} invio a proxy risposta")
    
    conn.send(to_proxy.encode("utf-8"))
    
    conn.close()


class Skeleton(Interface):
    def __init__(self, port):
        self.port = port
        
    @abstractmethod
    def inverti_stringa(self, data):
        pass
    
    def run_skeleton(self):
        ssocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        ssocket.bind(("0.0.0.0", self.port))
        
        info = ssocket.getsockname()
        
        print(f"{{SKELETON}} in ascolto su {info[0]} e porto: {info[1]}")
        
        ssocket.listen()
        
        while True:
            conn, addr = ssocket.accept()
            print("{SKELETON} avvio thread")
            td = threading.Thread(target=run_function, args=(conn, self))
            td.start()
            
            
        ssocket.close()