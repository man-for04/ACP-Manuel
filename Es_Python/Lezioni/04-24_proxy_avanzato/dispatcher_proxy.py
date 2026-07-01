from dispatcher_service import IDispatcher
import socket

class DispatcherProxy(IDispatcher):
    #dovrebbe implementare solo logica di connessione con server
    
    
    def __init__(self, host, port):
        
        self.host = host
        self.port = int(port)
        
    def sendCmd(self, command):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print("sto per connettermi...")
        s.connect((self.host, self.port))
        #print("connesso!")
        
        request = "sendCmd-" + str(command)
        
        s.send(request.encode("utf-8"))
        
        risposta = s.recv(1024).decode("utf-8")
        
        s.close()
        
        return risposta
        
    def getCmd(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #qui sto creando un nuovo port ogni volta
        s.connect((self.host, self.port))
        
        request = "getCmd-"
        
        s.send(request.encode("utf-8"))
        
        risposta = s.recv(1024).decode("utf-8")
        
        s.close()
        
        return risposta