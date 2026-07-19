
from Skeleton import Skeleton


class BuildWorkerImpl(Skeleton):
    
    def runTests(self, projectData:dict):  # pyright: ignore[reportIncompatibleMethodOverride]
        
        presenza_main = False
        sorgente_python = False
        no_contenuti_vuoti = True
        
        print("runTests avviato!")
        
        if('main.py' in projectData.keys()):
            presenza_main=True
            print("Main trovato!")
        
        for x in projectData.keys():
            
            if (('.py' in x ) and ('.main' not in x)):
                sorgente_python=True
                print("sorgente diverso da main.py trovato")
        
        for x in projectData.values():
            
            if(x==''):
                print("Trovato file vuoto!")
                no_contenuti_vuoti=False
        
        return (presenza_main and sorgente_python and no_contenuti_vuoti)
    
    
    def checkStyle(self, projectData:dict):  # pyright: ignore[reportIncompatibleMethodOverride]
        
        print("checkStyle avviato!")
        
        if('README.md' in projectData.keys()):
            return True
        else:
            return False