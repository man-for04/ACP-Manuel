###main
from server_impl import serverImpl
from skeleton import Skeleton



if __name__ == '__main__':
    
    PORT = 1234 #è una scelta che posso fare, NON va messo nell'impl perchè sto mischiando buisness logic e ...
    
    """
    impl = serverImpl()
    skeleton = Skeleton(PORT, impl) #posso passare tutte le info che mi servono
    ##devo avviare lo skeleton -> spesso run_skeleton, mettere su la comunicazione lato servente (es. istanzia socket ecc)
    skeleton.run_skeleton()
     #devo vedere come fornire il servizio, la logica di buisness
     """
     
     ##ereditarietà
    impl = serverImpl(PORT)
    impl.run_skeleton()