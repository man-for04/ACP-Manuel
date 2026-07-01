from abc import ABC, abstractmethod

class Service(ABC):
    
    #ricorda di mettere i metodi astratti e l'eccezione da sollevare (def di interfaccia)
    @abstractmethod
    def deposita(self, message):
        raise NotImplementedError
    
    @abstractmethod
    def preleva(self):
        raise NotImplementedError
    
    #andrò a istanziare proxy lato dispatcher e skeleton lato server

    