#server.py
#deve avviare il serve e passare riferimento al delegato
from skeleton import Skeleton
from serverImpl import ServerImpl

if __name__ == "__main__":
    
    PORT = 0
    
    print("Server in avvio...")
    impl = ServerImpl()
    skeleton = Skeleton(impl, PORT)
    skeleton.run_skeleton()