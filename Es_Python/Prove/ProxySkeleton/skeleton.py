from serverInterface import ServerInterface
import socket

import threading

class Skeleton(ServerInterface):
    """
    parametri: port, server_impl
    """
    
    def __init__(self, port, server_impl):
        
        self.port = port
        self.server_impl = server_impl
        
    def inverti_stringa(self, data):
        print("<SKELETON> inoltro a inverti_stringa del delegato...")
        r = self.server_impl.inverti_stringa(data)
        
        return r
    
    def run_skeleton(self):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', self.port))
        
        s.listen()
        
        print("<SERVER SKELETON> in ascolto su porto: ", self.port)
        
        while True:
            conn, addr = s.accept()
            
            #affido tutto al thread
            t = threading.Thread(target = run_function, args=(conn, self))
            
            t.start()
        
        s.close()
        
def run_function(conn:socket.socket, skeleton:Skeleton):
    
    richiesta = conn.recv(1024).decode("utf-8")
    
    risposta = skeleton.inverti_stringa(richiesta)
    
    #invia messaggio di risposta al client
    conn.send(risposta.encode("utf-8"))
    
    conn.close()
    