#skeleton.py
#parte + difficile --> devo creare connessione, accettare richieste del client, delegarle mediante riferimento a serverImpl
#che mi deve essere passato come parametro

from interface import SubjectInterface
from serverImpl import ServerImpl
import socket, threading
from time import sleep

def gestoreSocket(sock:socket.socket, skeleton_ref):
    print("{SKELETON} gestore avviato")
    from_proxy = sock.recv(4000).decode('utf-8')
    
    print(f'{{SKELETON}} ricevuto da client {from_proxy}')
    to_proxy = skeleton_ref.inverti_stringa(from_proxy)
    
    sock.send(to_proxy.encode('utf-8'))
    print(f'{{SKELETON}} inviata al client risposta {to_proxy}')
    
    sock.close()

class Skeleton(SubjectInterface):
    
    def __init__(self, delegate:ServerImpl, port):
        self.delegate = delegate
        self.port = port
        
    def inverti_stringa(self, data):
        return self.delegate.inverti_stringa(data)
    
    def run_skeleton(self):
        #creare connessione
        ssocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        ssocket.bind(("0.0.0.0", self.port))
        
        info = ssocket.getsockname()
        
        print(f'{{SKELETON}} in ascolto su {info[0]} e porto: {info[1]}')
        
        ssocket.listen()
        
        i=0
        while i<5:
            print(".")
            conn, addr = ssocket.accept()
            td = threading.Thread(target=gestoreSocket, args=(conn, self))
            td.start()
            
            i+=1
        
        sleep(5)
        ssocket.close()