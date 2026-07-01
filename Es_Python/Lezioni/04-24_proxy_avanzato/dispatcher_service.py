#INTERFACCIA BASE DEL SERVER | E' la soluzione con ereditarietà!

from abc import ABC, abstractmethod #sono fondamentali per definire interfaccia formale

class IDispatcher(ABC):
    #sendCMd(commando)
    @abstractmethod
    def sendCmd(self, command):
        pass
    
    #getCmd()
    @abstractmethod
    def getCmd(self):
        pass
    
    