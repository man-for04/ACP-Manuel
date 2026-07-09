import requests

from IValidationHub import IValidationHub

class VH_Impl(IValidationHub):
    #deve banalmente implementare il metodo
    
    def __init__(self, channel) -> None:
        super().__init__()
        self.channel = channel
    
    def submitProject(self, Project:dict):  # pyright: ignore[reportIncompatibleMethodOverride]
        
        print("-->Richiesta validazione: ")
        for key, values in Project.items():
            print(f'{key}:{values}')
        
        #check preliminari
        file_univoci = []
            
        if(len(Project.keys()) == 0): #se è vuoto, non ha chiavi!
            
            #check 1
            print("ERRORE! Dizionario vuoto")
            return False
        else:
            valori = Project.values()
            for x in valori:
                if(len(x)==0):
                    print("ERRORE! Lista di file vuota")
                    return False
                
                else:
                    for file in x:
                        if file not in file_univoci:
                            
                            file_univoci.append(file)
                        else:
                            print(f'ERRORE! Il file {file} è duplicato')
                            return False
            
        #Si è molto artigianale, ma dovrebbe andare (se ho tempo lo miglioro)
            
        #TODO: 2 richieste RESTFUL
        projectId = ''
        for x in Project.keys():
            projectId = str(x)
            
        
        controllo_runs = (requests.post(url=f'http://127.0.0.1:5000/projects/{projectId}/test-runs', json=Project)).json()
        controllo_checks = (requests.post(url=f'http://127.0.0.1:5000/projects/{projectId}/style-checks', json=Project)).json()
        
        controllo = {'result': 'pass'}
        
        x = (controllo_runs == controllo and controllo_checks == controllo)
        print("<VH_Impl>  controllo da flask è: ", x)
        
        if x ==True:
            self.channel.write(f'[{projectId}]-[pass]\n')
            self.channel.flush()
            print("scritto")
        else:
            self.channel.write(f'[{projectId}]-[fail]\n')
            self.channel.flush()
            print("scritto")
            
        return x