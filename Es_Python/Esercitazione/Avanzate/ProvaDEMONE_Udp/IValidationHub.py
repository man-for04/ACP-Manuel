from abc import ABC, abstractmethod

class IValidationHub(ABC):
    
    @abstractmethod
    def submitProject(self,Project):
        """
        Project:{
                (projectId:str) :  (file:str[] (valore, in numero e nome random)__________________      )
                .}
        """
        