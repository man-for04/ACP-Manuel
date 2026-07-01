#deve semplicemente avviare tutto
from server_impl import ServerImpl
from skeleton import Skeleton

if __name__ == '__main__':
    print("Sono il server")
    ADDRESS = 'localhost'
    PORT = 1234
    
    server_impl = ServerImpl()
    skeleton = Skeleton(PORT, server_impl)
    
    skeleton.run_skeleton()