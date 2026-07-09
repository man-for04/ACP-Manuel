#implementatore
from multiprocessing import Process, Queue

from Printer_skeleton import Printer_skeleton

def produttore(queue:Queue, pathFile:str, tipo:str):
    to_insert = pathFile+'-'+tipo
    queue.put(to_insert)
    print("== Inserito in coda ", to_insert)

class PrinterImpl(Printer_skeleton):
    
    def __init__(self, queue) -> None:
        super().__init__()
        self.queue = queue
    
    def print_function(self, pathFile, tipo):
        #implementazione
        p = Process(target=produttore , args=(self.queue, pathFile, tipo))
        p.start()
        #@Gemini: qui non va messa la join, giusto?