#IMPLEMENTA LA LOGICA DI COMUNICAZIONE LATO SERVER (l'altra metà del proxy-skeleton) | DEVE AVERE UN RIF AL VERO SERVER

from interface import Subject
import socket, threading


def run_function(conn, skeleton_ref:Skeleton):
    
    #va gestita la parte di comunicazione: ricevi il dato, chiama il delegato, manda la risposta
    data = conn.recv(1024)
    result = skeleton_ref.inverti_stringa(data)
    conn.send(result)
    conn.close()

class Skeleton(Subject): #implemento di fatto l'interfaccia
    
    #avrò costruttore, che inzializza istanza di implementatore, effettuerà la delega, avrà metodo run_skeleton per metter su la comunicazione
    def __init__(self, port, delegate): #il riferimento all'oggetto delegate va messo!
        self.port = port
        self.delegate = delegate #è un nome che scelgo io, si riferisce all'oggetto impl che ho passato
        
    def inverti_stringa(self, data):
        """
        aaa
        """
        #tale metodo è descritto, NON implementato nell'interfaccia;
        #lo skeleton lo implementa ma non veramente (lo delega)
        return self.delegate.inverti_stringa(data) #ottengo la stringa invertita che a mia volta ritornerò | non ci sarà in ereditarietà
    
    def run_skeleton(self): #mettere su la comunicazione
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("localhost", self.port))
        s.listen()
        
        print("Ciao 🦴")
        print("SERVER LISTENING ON PORT ", self.port)
        
        while True:
            conn, addr = s.accept()
            
            #affida a un thread🧵 la gestione della socketina🧦
            t = threading.Thread(target=run_function, args=(conn, self))#va passato l'oggetto da utilizzare per la delega, è proprio ciò a cui serve lo skeleton
                                                        #🧦 NON METTERE run_function() -> chiama a funzione e dà problemi per l'assenza di parametri
            t.start()
            
        s.close()