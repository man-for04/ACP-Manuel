
import json
import socket

from IBuildWorker import IBuildWorker


class ValidationProxy(IBuildWorker):
    
    def __init__(self, porto) -> None:
        self.porto = int(porto)
    
    #devono inviare su socket tcp
    def runTests(self, projectData : dict):  # pyright: ignore[reportIncompatibleMethodOverride]
        
        conn = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        conn.connect(('localhost', self.porto))
        
        projectData['metodo'] = 'runTests'
        
        conn.send(json.dumps(projectData).encode('utf-8'))
        print("<-- <proxy> invio runTests effettuato!")
        
        ret = (conn.recv(4000).decode()).strip()
        
        ret_bool = False
        
        if('True' in ret):
            ret_bool = True
        
        
        print(f"--> <Proxy> ricevuto da BuildWorker: str:{ret}, bool: {ret_bool}")
        
        conn.close()
        
        return ret_bool
    
    def checkStyle(self, projectData : dict):  # pyright: ignore[reportIncompatibleMethodOverride]
        
        conn = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        conn.connect(('localhost', self.porto))
        
        projectData['metodo'] = 'checkStyle'
        
        conn.send(json.dumps(projectData).encode('utf-8'))
        print("<-- <proxy> invio runTests effettuato!")
        
        ret = (conn.recv(4000).decode()).strip()
        
        ret_bool = False
        
        if('True' in ret):
            ret_bool = True
        
        print(f"--> <Proxy> ricevuto da BuildWorker: str:{ret}, bool: {ret_bool}")
        
        conn.close()
        
        return ret_bool