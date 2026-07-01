#client.py
#deve istanziare proxy e chiamarlo

import sys
from proxy import Proxy

if __name__ == "__main__":
    
    try:
        PORT = int(sys.argv[1])
        STRING = sys.argv[2]
        
    except (IndexError, ValueError):
        print("Errore parametri invocazione")
        
    proxy = Proxy(PORT)
    print("{CLIENT} invocato Proxy")
    ret = proxy.inverti_stringa(data=STRING)
    
    print(f'{{CLIENT}} ricevuto da proxy {ret}')