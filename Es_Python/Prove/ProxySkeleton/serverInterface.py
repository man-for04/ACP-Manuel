from abc import ABC, abstractmethod

class ServerInterface(ABC):
    
    @abstractmethod
    def inverti_stringa(self, data):
        pass