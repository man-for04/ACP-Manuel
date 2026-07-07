from multiprocessing import Process, Queue, current_process, Lock
import time

import stomp


class MioListener(stomp.ConnectionListener):
    
    def __init__(self,queue) -> None:
        
        super().__init__()
        self.queue : Queue = queue #coda (gpu o rt a seconda del processo che ha creato il listener)
        
        print(f"Sono listener di {current_process().name}")
    
    def on_message(self, frame):
        
        msg : str = frame.body
        if("deploy" in msg):
            print("<Listener> deploy attivato")
            try:
                
                id = msg.split('-')[1]
                name = msg.split('-')[2]
                
                to_deploy : str = str(id)+'-'+str(name)
                try:
                    self.queue.put(to_deploy, timeout=2)
                except Exception:
                    print(f"TIMEOUT PER CODA PIENA, messaggio {to_deploy} scartato")
                print(f"Processo: {current_process().name}: Inserito sulla queue messaggio <{to_deploy}>")
                
            except TypeError:
                print("ERRORE TIPI NEL LISTENER")
        
        elif("stop_all" in msg):
            print("<Listener> stop_all attivato")
            #Non è necessario gestire la concorrenza, sono l'unico processo che può accedere a questa coda
            while( not self.queue.empty()):
                x = self.queue.get()
                print(f"Processo: {current_process().name}: Rimosso dalla coda <{x}>")
            print(f"Processo: {current_process().name} coda svuotata!")
            
        else:
            print("ERRORE! Operazione non riconosciuta!")

def run_gpu_proc(gpu_queue):
    conn = stomp.Connection([('localhost', 61613)], auto_content_length=False)
    conn.set_listener("",MioListener(queue=gpu_queue))
    conn.connect(wait=True)
    conn.subscribe(destination="/topic/gpu", id=1, ack='auto')

    print("Listener GPU settato!")
    
    time.sleep(40)
    conn.disconnect()

def run_rt_proc(rt_queue):
    conn = stomp.Connection([('localhost', 61613)], auto_content_length=False)
    conn.set_listener("",MioListener(queue=rt_queue))
    conn.connect(wait=True)
    conn.subscribe(destination="/topic/rt", id=1, ack='auto')

    print("Listener RT settato!")
    
    time.sleep(40)
    conn.disconnect()


if __name__ == "__main__":
    
    #code per i topic
    gpu_queue =Queue(5)
    rt_queue = Queue(5)
    
    gpu_proc = Process(name="GPU", target=run_gpu_proc, args=(gpu_queue,))
    rt_proc = Process(name="RT", target=run_rt_proc, args=(rt_queue,))
    
    gpu_proc.start()
    rt_proc.start()
    
    print("Processi attivati")
    gpu_proc.join()
    rt_proc.join()
    
    print("Worker terminato!")
