import random

from Proxy import Proxy
import sys
import uuid

from random import randint

def genera_progetto():
    
    print("Genero progetto univoco...")
    
    possibili_file = ['main','README', 'unina'] #7
    possibli_estensioni = ['.md', '.py'] #2
    
    projectId = f'pro-{randint(1000, 9999)}'
    numero_file = randint(1,3)
    file = []
    
    for _ in range(numero_file):
        file.append(f'{possibili_file[randint(0,2)]}{possibli_estensioni[randint(0,1)]}')
        
    Project = {projectId:file}
    return projectId, Project

if __name__ == "__main__":
    
    port = int(sys.argv[1])
    print("In ascolto su porto", port)
    
    proxy = Proxy(port=port)
    
    id_univoci = []
    
    for i in range(5):
        
        key, Project = genera_progetto()
        
        while(key in id_univoci):
            key, Project = genera_progetto()
            
        id_univoci.append(key)
        
        ris = proxy.submitProject(Project)
        
        print("--> Ricevuto risposta ACK: ", ris)
    
    