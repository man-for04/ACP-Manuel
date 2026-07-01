import sys
from datetime import datetime
from dispatcher_proxy import DispatcherProxy #dovrò istanziare un Proxy

if __name__ == "__main__":
    
    try: 
        HOST = sys.argv[1]
        PORT = sys.argv[2]
        
    except IndexError:
        print("Please, specify HOST/PORT args...")
        sys.exit(-1)
        
    dict_cmd = {0:"leggi", 1:"scrivi", 2: "configura", 3:"reset"}
        
    while True:
        
        #crea oggetto Proxy e invocare getCmd
        
        proxy = DispatcherProxy(HOST, PORT) #perchè creare un nuovo proxy? Il client ( e quindi la socket) è sempre diverso
        comando = proxy.getCmd()
        
        with open("cmd.log", mode='a') as f:
            
            f.write(f'{datetime.now()} {dict_cmd[int(comando)]}\n')
            