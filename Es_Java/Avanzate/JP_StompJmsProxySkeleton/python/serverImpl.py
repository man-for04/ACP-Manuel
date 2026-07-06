
from multiprocessing import Queue

from serverSkeleton import serverSkeleton


class serverImpl(serverSkeleton):
    
    def deposita(self, valore):
        """
        public void deposita(int valore);
        """
        print("<ServerImpl> depositando valore ", valore)
        self.queue.put(valore)
        
    
    def preleva(self):
        """
        public int preleva();
        """
        print("Prelevo da queue...")
        val =self.queue.get()
        print("<ServerImpl> prelevato valore da queue ", val)
        return val
