from dispatcher_service import IDispatcher
from abc import ABC, abstractmethod
import socket, multiprocessing as mp


def run_function(conn, skeleton):
    #ricevere su socket richiesta di client/actuator
    
    ### sendCmd-0, sendCmd#1 -> la cosa + semplice è usare un carattere separatore e alla ricezione splittare la stringa su tale stringa
    
    message = conn.recv(1024).decode("utf-8")#riceverò da client o actuator
    
    #"sendCmd-0".split(-) => ('sendCmd', '0')
    request = message.split('-')[0]
    
    print(f'DISPATCHER_SKELETON request {request} ricevuta')
    
    if request == "sendCmd":
        #chiama la sendCmd attraverso lo skeleton per invocare ssendCmd dell'impl
        command = message.split('-')[1]
        skeleton.sendCmd(command) 
        #prevedi sempre una richiesta/risposta del client, manda sempre qualcosa indietro al client (anhce solo un ACK) per sicurezza
        result = "ACK"
        
    elif request == "getCmd" :
        ##...
        result = skeleton.getCmd()
        
    else:
        ##
        result = "ERROR"
        
    conn.send(str(result).encode("utf-8"))
    
    conn.close()

class DispatcherSkeleton(IDispatcher, ABC): #estende interfaccia e è astratta
    def __init__(self, host, port):
        self.host = host
        self.port = port
        
    #in teoria dovrebbe non servire, ma per sicurezza mettili:
    @abstractmethod
    def sendCmd(self, command):
        pass
    
    @abstractmethod
    def getCmd(self):
        pass
    
    def run_skeleton(self):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        
        print(f'DISPATCHER_SKELETON bind to {(self.host, self.port)}')
        
        s.listen()#dovrebbe scegliere in automatico la dim
        print(f'DISPATCHER_SKELETON listening...')
        
        while True:
            
            c, addr = s.accept() #c la posso chiudere qui dopo p.start() [ma dovrei aspettare la terminazione del p] o meglio, direttamente nella run_function()
            print(f"DISPATCHER_SKELETON accepted connection from {addr}")
            
            p = mp.Process(target=run_function, args=(c, self)) #devo ricordarmi di passare il riferimento all'ggetto corrente per poter usare sendCmd e getCmd [chiamare i metodi dell'implementazione]
            p.start() #qui viene fatta spawn/fork/forkserver-- RICORDALO!
            c.close()
            
        s.close()
        