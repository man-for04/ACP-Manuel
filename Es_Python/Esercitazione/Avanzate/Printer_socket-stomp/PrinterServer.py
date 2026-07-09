from multiprocessing import Queue, Process

from PrinterImpl import PrinterImpl

def consumatore(queue:Queue):
    print("Sono il processo consumatore")
    
    while(True):
        elem = queue.get()
        print(f"== consumato {elem}, preparo STOMP..")
        
        #TODO: Invia su STOMP
    

if __name__ == "__main__":
    
    queue = Queue(5)
    server = PrinterImpl(queue=queue)
    
    
    p = Process(target=consumatore, args=(queue, ))
    p.start()
    
    server.run_skeleton()
