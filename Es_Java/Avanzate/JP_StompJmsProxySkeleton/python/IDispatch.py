from abc import ABC, abstractmethod

class IDispatch(ABC):
    
    @abstractmethod 
    def deposita(self, valore):
        """
        public void deposita(int valore);
        """
        raise NotImplementedError
    
    @abstractmethod
    def preleva(self):
        """
        public int preleva();
        """
        raise NotImplementedError