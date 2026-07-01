###istanziare un dispatcher impl
### e lanciare lo skeleton

### skeleton è per interitance

import sys
from dispatcherImpl import dispatcherImpl

if __name__ == "__main__":
    
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    
    dispatcherImpl = dispatcherImpl(HOST, PORT)
    dispatcherImpl.run_skeleton() #uso socket? Passo IP,Porto (es in ingresso dalla command line)