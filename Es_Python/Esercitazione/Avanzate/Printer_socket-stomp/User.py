import time

from proxy import proxy
import sys
from random import randint

if __name__ == "__main__":
    
    #passare su args il porto del server
    porto = int(sys.argv[1])
    print("Invio richieste su: ", porto)
    
    mioProxy = proxy(port=porto)
    
    possibili_estensioni = ['doc', 'txt']
    possibili_tipi = ['bw', 'gs', 'color']
    
    for i in range(10):
        pathFile = f'/user/file_{randint(0,100)}.{possibili_estensioni[randint(0,1)]}'
        tipo = possibili_tipi[randint(0,2)]
        
        mioProxy.print_function(pathFile, tipo)
        
        time.sleep(1)