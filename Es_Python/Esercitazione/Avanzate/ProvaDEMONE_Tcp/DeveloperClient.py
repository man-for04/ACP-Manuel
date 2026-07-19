import sys

import IValidationHub_pb2
import IValidationHub_pb2_grpc
import grpc

import uuid
import random



def genera_richiesta():
    
    filenames = ['main.py', 'README.md', 'ciao.py', 'helloooo.py', 'ldesi.py', 'unina', 'ok']
    """
    funzione di utilità per inviare in 1 stream 5 messaggi"""
    projectId = str(uuid.uuid1())
    
    for i in range(5):
        fileName = filenames[random.randint(0,6)]
        content = f'contenuto_{random.randint(1,99)}'
        chunkIndex = int(i)
        
        print(f"<-- Costruito: <projectId:{projectId}, fileName:{fileName}, content:{content}, chunkIndex:{chunkIndex}>")
        
        msg = IValidationHub_pb2.CodeChunk(projectId=projectId, fileName=fileName, content=content, chunkIndex=chunkIndex)
        yield msg

if __name__ == "__main__":
    
    with grpc.insecure_channel('localhost:'+sys.argv[1]) as channel:
        
        stub = IValidationHub_pb2_grpc.ValidationStub(channel)
        
        to_hub = genera_richiesta()
        
        print("<--Invio...")
        
        from_hub = stub.submitProject(to_hub)
        
        print("--> Risultato dell'invio: ", from_hub.result)
        
        