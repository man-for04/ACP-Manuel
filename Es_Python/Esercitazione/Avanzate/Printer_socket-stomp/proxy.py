from IPrinter import IPrinter
import socket

class proxy(IPrinter):
    
    def __init__(self, port) -> None:
        super().__init__()
        self.port = int(port)
    
    def print_function(self, pathFile, tipo):
        #impelmenta cmìomunicazione su socket TCP
        
        conn = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        
        conn.connect(('localhost', self.port))
        
        print("User connesso!")
        
        to_server = f'{pathFile}#{tipo}'
        print(f"<-- Inviando {to_server}")
        conn.send(to_server.encode('utf-8'))
        
        
        conn.close()