#coda process-safe prodcons

from multiprocessing import Condition, Lock

class miaCoda():
    def __init__(self, DIM_MAX) -> None:
        self.DIM_MAX = DIM_MAX
                
        self.buffer = []
        
        self.lock = Lock()
        
        self.cv_prod = Condition(lock=self.lock)
        self.cv_cons = Condition(lock=self.lock)
        
    def inserisci(self, elem):
        
        with self.lock: #entra nel monitor
            while self.is_full():
                #in attesa
                self.cv_prod.wait()
            
            #sezione critica
            self.buffer.append(elem)
            print(f"{elem} inserito in coda")
            
            self.cv_cons.notify()
    
    def svuota(self):
        lista = []
        with self.lock:
            while self.is_empty():
                print("<coda> prelevando mi metto in attesa")
                #in attesa
                self.cv_cons.wait()
                print("<coda> sbloccato")
                
            #sez critica
            print("<coda> sono dentro per svuotare")
            for x in self.buffer:
                lista.append(x)
                print(f'{x} rimosso dalla coda')
            
            self.buffer.clear()
            print("coda svuotata")
            
            self.cv_prod.notify_all()
        return lista
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def is_full(self):
        return len(self.buffer)==self.DIM_MAX