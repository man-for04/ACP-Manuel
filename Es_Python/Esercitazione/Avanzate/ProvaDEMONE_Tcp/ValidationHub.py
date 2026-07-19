from concurrent.futures import ThreadPoolExecutor
import sys

from Proxy import ValidationProxy
import IValidationHub_pb2
import IValidationHub_pb2_grpc
import grpc

class ValidationImpl(IValidationHub_pb2_grpc.ValidationServicer):
    
    try:
        #impl il servizio
        
        def __init__(self, out, proxy : ValidationProxy) -> None:
            self.out = out
            self.proxy = proxy
        
        def submitProject(self, request_iterator, context):
            
            vuoto = True
            IdPresente = True
            FileVuoti = False
            FileDuplicati = False
            
            fileUnivoci = []
            
            projectData = {}
            
            projectId=''
            
            for from_client in request_iterator:
                
                vuoto = False
                
                projectId = str(from_client.projectId)
                fileName = str(from_client.fileName)
                content = str(from_client.content)
                chunkIndex = int(from_client.chunkIndex)
                
                print(f'--> Ricevuto da client <projectId:{projectId}, fileName:{fileName}, content:{content}, chunkIndex:{chunkIndex}>')
                
                #test vari
                if(projectId ==''):
                    IdPresente = False
                
                if(fileName == ''):
                    FileVuoti =  True
                    
                if (fileName not in fileUnivoci):
                    fileUnivoci.append(fileName) #lista per il check
                    projectData[fileName] = content #dizionario per i metodi, coppie filename/content
                    
                else:
                    FileDuplicati=True
                
                    
            #verifico i flag
            if((not vuoto) and IdPresente and (not FileVuoti) and (not FileDuplicati)):
                print("Tutti i controlli ok!")
                
                
                ris1 = bool(self.proxy.checkStyle(projectData))
                ris2 = bool(self.proxy.runTests(projectData))
                
                
                to_client = ris1 and ris2
                
                if to_client is True:
                    to_write = f'[{projectId}]-[success]\n'
                else:
                    to_write = f'[{projectId}]-[fail]\n'
                
                self.out.write(to_write)
                self.out.flush()
                
                print("<-- Invio risposta: ", to_client)
                return IValidationHub_pb2.ValidationResult(result=to_client)
                
            
            else:
                print("ERRORE! Qualche check è andato storto!")
                return IValidationHub_pb2.ValidationResult(result=False)
    except Exception as e:
        print(e)
        print("ERRORE nell'impl di grpc")
        
if __name__ == "__main__":
    
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    
    porto = int(sys.argv[1])
    
    with open('log.txt', 'a') as out:
        
        proxy = ValidationProxy(porto)
        servicer = ValidationImpl(out=out, proxy=proxy)
        
        IValidationHub_pb2_grpc.add_ValidationServicer_to_server(servicer, server)
        port = server.add_insecure_port('0.0.0.0:0')
        print("Server listening on: ", port)
        
        server.start()
        
        server.wait_for_termination()