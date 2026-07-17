from abc import ABC, abstractmethod

class IBalancer(ABC):
    @abstractmethod
    def request(self, tipo, domain, endpoint):
        raise NotImplementedError