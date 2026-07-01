
from dispatcherSkeleton import DispatcherSkeleton
import multiprocessing as mp

class dispatcherImpl(DispatcherSkeleton): #deve implementare metodi
    
    
    def __init__(self, host, port, queue = mp.Queue(5)): #devo anche tenere in considerazione il costruttore del padre
                                                      #sulla queue è una scelta: posso anche crearla allinterno o passarla dal 
                                                      # main --> la coda NON va messa nello skeleton, perchè è parte della buisness logic
        super().__init__(host, port) 
        self.queue = queue #va aggiunto questo attributo
        
    #i 2 metodi agiranno su una CODA:
    
    #metodo impl di sendCmd, che lavorano su queue
    def sendCmd(self, command):
        print(f'DISPATCHER_IMPL sendCmd{command} da produrre')
        self.queue.put(command)
    
    #metodo impl di getCmd
    def getCmd(self):   # è qui che posso dover implementare mutua esclusione o altro
        ret = self.queue.get()
        print(f'DISPATCHER_IMPL getCmd return {ret}')
        return ret
        