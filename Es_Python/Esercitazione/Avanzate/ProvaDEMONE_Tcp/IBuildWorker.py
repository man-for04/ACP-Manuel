from abc import ABC, abstractmethod

class IBuildWorker(ABC):
    
    @abstractmethod
    def runTests(self,projectData):
        pass
    
    @abstractmethod
    def checkStyle(self, projectData):
        pass