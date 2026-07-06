#TODO: Run skeleton

from abc import ABC, abstractmethod
from multiprocessing import Process
import socket
from time import sleep

from IDispatch import IDispatch

def run_process(s:socket.socket, skel):
    mess_richiesta = s.recv(1024).decode("utf-8").strip()
    print(f"<ServerSkeleton> ricevuto messaggio {mess_richiesta}")
    
    tipo_richiesta = mess_richiesta.split('#')[0]
    print(f'Tipo richiesta: <{tipo_richiesta}>')
    
    if ("preleva" in mess_richiesta):
        #caso 1-> soltanto richiesta di prelevare
        ris = str(skel.preleva()+'\n')
        s.send(ris.encode("utf-8"))
        
        print(f'<ServerSkeleton> ho inviato risposta a richiesta: {ris}')
        
        
    elif ("deposita" in mess_richiesta):
        val_da_depositare = int(mess_richiesta.split('#')[1])
        
        print(f'Richiesta di depositare {val_da_depositare} ricevuta')
        skel.deposita(val_da_depositare)
        
        ris = "ack\n"
        s.send(ris.encode("utf-8"))
        
    else:
        print("ERRORE! Tipologia di richiesta non valida!")
        ris = "ERROR\n"
        s.send(ris.encode('utf-8'))
        
    sleep(1)
    s.close()
    

class serverSkeleton(IDispatch, ABC):
    def __init__(self, port, queue) -> None:
        self.port = port
        self.queue = queue #una coda mp per gestire la memorizzazione dei dati inviati
    
    def run_skeleton(self):
        print("Ciao, sono lo skeleton")
        
        #gestire connessione con client e passare socket di connessione ai process
        sserver = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        sserver.bind(("0.0.0.0", self.port))
        
        sserver.listen()
        info = sserver.getsockname()
        print(f"Server listening on port: {info[1]}")
        
        while(True):
            conn, addr = sserver.accept()
            p = Process(target=run_process, args=(conn, self))
            p.start()
            
        sserver.close()
        
    
    
    @abstractmethod 
    def deposita(self, valore):
        """
        public void deposita(int valore);
        """
        raise NotImplementedError
    
    @abstractmethod
    def preleva(self):
        """
        public int preleva();
        """
        raise NotImplementedError
    
    