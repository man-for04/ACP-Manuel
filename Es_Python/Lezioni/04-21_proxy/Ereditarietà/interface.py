#UGUALE PER EREDITARIETA' O DELEGA
from abc import ABC, abstractmethod

class Subject(ABC):
    #tutti i metodi astratti che sono i miei servizi
    
    @abstractmethod
    def inverti_stringa(self, data):
        pass #