from IValidationHub import IValidationHub
import socket

class Proxy(IValidationHub):
    
    def __init__(self, port) -> None:
        super().__init__()
        self.port = port
        
    def submitProject(self, Project:dict):  # pyright: ignore[reportIncompatibleMethodOverride]
        #inviare richiesta
        conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        key = ''
        
        for _ in Project.keys():
            key = _
        
        to_server = f'{key}'
        
        elenco_file = Project[key]
        
        for file in elenco_file:
            to_server = f'{to_server}#{file}'
            
        print("<-- Invio a server: ", to_server)
            
        conn.sendto(to_server.encode('utf-8'), ('127.0.0.1', self.port))
        
        reply, add = conn.recvfrom(4000)
        
        conn.close()
        return (reply.decode('utf-8'))