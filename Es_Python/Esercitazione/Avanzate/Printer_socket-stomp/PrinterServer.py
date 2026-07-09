from multiprocessing import Queue, Process

from PrinterImpl import PrinterImpl
import stomp

def consumatore(queue:Queue):
    print("Sono il processo consumatore")
    
    #setup STOMP connection
    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.connect(wait=True)
    
    while(True):
        elem = queue.get()
        print(f"== consumato {elem}, preparo STOMP..")
        
        #Invia su STOMP
        if('color' in elem):
            
            conn.send(destination='/queue/color', body=elem)
            
        elif('bw' in elem or 'gs' in elem):
            
            conn.send(destination='/queue/bw', body=elem)
            
        else:
            print("ERRORE! Tipo non riconosciuto: ", elem)
            
    conn.disconnect()
    

if __name__ == "__main__":
    
    queue = Queue(5)
    server = PrinterImpl(queue=queue)
    
    
    p = Process(target=consumatore, args=(queue, ))
    p.start()
    
    server.run_skeleton()
