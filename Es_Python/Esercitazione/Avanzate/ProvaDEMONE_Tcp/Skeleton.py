
import json
import re
import socket
from threading import Thread
from abc import ABC

from IBuildWorker import IBuildWorker

def skeletonThread(conn:socket.socket, rif):
    
    try:
    
        from_hub = (conn.recv(4000)).decode('utf-8')
        
        projectData : dict = json.loads(from_hub)
        
        print("\n--> Ho ottenuto un dizionario? ", type(projectData))
        
        for key, value in projectData.items():
            print(f'{key} : {value}')
            
            
            
        if(projectData['metodo'] == 'runTests'):
            
            print("<skeleton> chiamo runTests()")
            
            ret = str(rif.runTests(projectData))
            
            print("<-- <skeleton> invio risultato runTests: ", ret)
            
            conn.send(ret.encode('utf-8'))
            conn.close()
            
        elif(projectData['metodo'] == 'checkStyle'):
            
            print("<skeleton> chiamo checkStyle()")
            
            ret = str(rif.checkStyle(projectData))
            
            print("<-- <skeleton> invio risultato checkStyle: ", ret)
            
            conn.send(ret.encode('utf-8'))
            conn.close()
            
        else:
            
            print("ERRORE! Richiesta non valida")
            
            ret = str(False)
            
            conn.send(ret.encode('utf-8'))
            conn.close()
            
            
    except (IndexError, ValueError) as e:
        print("ERRORE IN SPACCHETTAMENTO JSON")


class Skeleton(IBuildWorker, ABC):
    
    #deve solo gestire la comunicazione, poi chiamaare su sè stesso (ereditarietà) il metodo
    #passa ai thread un rif "self"
    
    def run_skeleton(self):
        serversocket= socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        
        serversocket.bind(('0.0.0.0',0))
        
        add, porto = serversocket.getsockname()
        
        serversocket.listen()
        print("Server listening on: ", add, ", porto: ", porto)
        
        while True:
            conn, addr = serversocket.accept()
            td = Thread(target=skeletonThread, args = (conn, self))
            td.start()
            
    