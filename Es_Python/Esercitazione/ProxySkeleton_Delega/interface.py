#interface.py
from abc import ABC, abstractmethod

class SubjectInterface(ABC):
    
    @abstractmethod
    def inverti_stringa(self, data):
        pass