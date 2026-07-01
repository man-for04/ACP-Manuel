###main


from server_impl import serverImpl
from skeleton import Skeleton



if __name__ == '__main__':
    
    #parte relativa all'attivazione skeleton
    ###1. istanziare un oggetto dell'impl
    ###2. istanziare uno skeleton a cui passare un riferimento dell'impl, per poter fare la delega | in ereditarietà basta 1 sola istanziazione
    ###3. far partire uno skeleton, devo attivare la parte di ascolto delle richieste
    
    PORT = 1234 #è una scelta che posso fare, NON va messo nell'impl perchè sto mischiando buisness logic e ...
    
    impl = serverImpl()
    skeleton = Skeleton(PORT, impl) #posso passare tutte le info che mi servono
    ##devo avviare lo skeleton -> spesso run_skeleton, mettere su la comunicazione lato servente (es. istanzia socket ecc)
    skeleton.run_skeleton()
     #devo vedere come fornire il servizio, la logica di buisness