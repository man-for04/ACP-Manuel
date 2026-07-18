import sys

import Orchestration_pb2
import Orchestration_pb2_grpc
import grpc
import random


tipi_corretti = ['GPU-based', 'CPU-based']
tipi_errato = ['CPU-based', 'NPU-based']

def genera_gpu_cpu():
    #genera stream per 2 gpu e 2 cpu
    
    
    for x in range(4):
        #gpu
        
        indice = (x%2)
        print("Indice:" , indice)
        tipo =  str(tipi_corretti[indice])
        task = f'TASK-{random.randint(1,50)}'
        
        print(f"<-- Invio <{tipo} , {task}>")
        
        msg = Orchestration_pb2.msg_req(tipo=tipo, task=task)
        print("creato")
        
        yield msg
        
    print("done")
        
        
def genera_cpu_nv():
    
    for a in range(4):
        #gpu
        indice = a%2
        print("Indice:" , indice)
        tipo =  str(tipi_errato[indice])
        task = f'TASK-{random.randint(1,50)}'
        
        print(f"<-- Invio <{tipo} , {task}>")
        
        msg = Orchestration_pb2.msg_req(task=task, tipo=tipo)
        yield msg
        
    print("done")

if __name__ == "__main__":
    
    with grpc.insecure_channel("localhost:"+sys.argv[1]) as channel:
        
        stub = Orchestration_pb2_grpc.OrchestrationStub(channel=channel)
        
        invio1 = genera_gpu_cpu()
        invio2=genera_cpu_nv()
        
        ris1 = stub.orchestrate(invio1)
        
        ris2 = stub.orchestrate(invio2)
        
        print("--> Ricevuto risposta a gpu/cpu: ", ris1)
        print("--> RIcevuto risposta a cpu/npu: ", ris2)