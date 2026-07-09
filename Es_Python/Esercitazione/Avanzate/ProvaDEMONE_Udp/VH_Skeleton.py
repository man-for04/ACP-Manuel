from threading import Thread

from VH_Impl import VH_Impl
from IValidationHub import IValidationHub
from abc import ABC
import socket

def validation(data, add, conn:socket.socket, ske):
    from_client = str(data.decode('utf-8'))
    
    #è stringa, va spacchettata!
    elementi = from_client.split('#')
    
    Project = {}
    
    try:
        print("\n\n")
        key = str(elementi.pop(0))
        #@Gemini: in fase di passaggio dict-> string, avrei potuto usare il .join sui nomi dei file?
        Project[key] = elementi
        
        to_client_bool = str(ske.submitProject(Project))
        
        to_client = to_client_bool.encode('utf-8')
        
        print("<-- Rispondo a client ", to_client_bool)
        
        conn.sendto(to_client, add)
        
        
    except (ValueError, IndexError):
        print("ERRORE in conversione string-> dict")


class VH_Skeleton(IValidationHub, ABC):
    
    def __init__(self, rif:VH_Impl) -> None:
        super().__init__()
        self.rif = rif
        
    def submitProject(self, Project):  # pyright: ignore[reportIncompatibleMethodOverride]
        return self.rif.submitProject(Project)
        print("DELEGANDO")
    
    def run_skeleton(self):
        #deve avere un riferimento a impl
        #Gestione comunicazione su socket udp
        
        
        ssocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        ssocket.bind(('localhost', 0))
        
        info = ssocket.getsockname()
        
        print("Server in ascolto su: ", info[1])
        
        
        #passo i dati ricevuti (dati+indirizzo) e la socket di risposta al thread
        try:
            
            while True:
                data, add = ssocket.recvfrom(4000)
                td = Thread(target=validation, args=(data, add, ssocket, self)) #@Gemini: fammi sapere se è corretto passare self, l'alternativa sarebbe stata self.rif
                td.start()
        except KeyboardInterrupt:
            ssocket.close()
            print("Server terminato!")
