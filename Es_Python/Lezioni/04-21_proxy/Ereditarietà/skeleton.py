from interface import Subject
import socket, threading
from abc import ABC, abstractmethod


def run_function(conn, skeleton_ref):
    
    #va gestita la parte di comunicazione: ricevi il dato, chiama il delegato, manda la risposta
    data = conn.recv(1024)
    result = skeleton_ref.inverti_stringa(data) #chiama il metodo che l'erede implementerà
    conn.send(result)
    conn.close()


class Skeleton(Subject, ABC): #implemento di fatto l'interfaccia con ASTRATTA
    
    #avrò costruttore, che inzializza istanza di implementatore, effettuerà la delega, avrà metodo run_skeleton per metter su la comunicazione
        
    def __init__(self, port): #DIFFERENZA --> QUI NON HO IL RIF AL DELEGANTE
        self.port = port
    
    @abstractmethod   
    def inverti_stringa(self, data):
        pass
    
    def run_skeleton(self): #mettere su la comunicazione
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("localhost", self.port))
        s.listen()
        
        print("Ciao 🦴")
        print("SERVER LISTENING ON PORT ", self.port)
        
        while True:
            conn, addr = s.accept()
            
            t = threading.Thread(target=run_function, args=(conn, self)) 
                                                        #lo skeleton
                                                        #NON METTERE run_function() -> chiama a funzione e dà problemi per l'assenza di parametri
            t.start()
            
        s.close()