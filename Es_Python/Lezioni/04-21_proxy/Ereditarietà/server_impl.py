

#più suddivido in moduli, più leggibile è! Meglio scrivere le cose per bene
#from interface import Subject
from skeleton import Skeleton


class serverImpl(Skeleton): #--> DIFFERENZA: permette di implementare l'interfaccia, la classe serverImpl aderisce a quell'interfaccia
    
    def inverti_stringa(self, data):
        ###
        print("SERVER IMPL invocato inverti_Stringa", data)
        data = data[::-1] #posso usare approccio slicing per invertire facilmente
        return data
    
#ho creato un implementatore che sarà invocato dal server, quando arriverà la richiesta verrà fatta DELEGA a istanza di server_impl

##client e server devono usare la stessa codifica dei dati -> altrimenti comunicano, ma non possono interpreate i byte inviati

##Ereditarietà -> non devo più ....., ma estendere lo skeleton