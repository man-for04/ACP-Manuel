#interface.py
#definisco interfaccia che gli altri dovranno implementare, e basta
from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def inverti_stringa(self, data):
        pass