from multiprocessing import Process, Queue
from miaCoda import miaCoda

import stomp

def ticketProcess(frame, queue:Queue):
    from_manager = str(frame.body) #TODO: va?
    print("--> <ticketProcess> ricevuto: ", from_manager, ", lo metto in coda")
    #TODO: Inserisci in coda
    queue.put(from_manager)

class TicketsListener(stomp.ConnectionListener):
    
    def __init__(self, queue) -> None:
        super().__init__()
        self.queue=queue
        
        
    def on_message(self, frame):
        
        p = Process(target=ticketProcess, args=(frame, self.queue))
        p.start()
        
        print("ticketProcess finito")