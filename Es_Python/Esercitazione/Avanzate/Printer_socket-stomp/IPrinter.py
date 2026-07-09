from abc import ABC, abstractmethod

class IPrinter(ABC):
    
    @abstractmethod
    def print_function(self, pathFile, tipo):
        raise NotImplementedError()