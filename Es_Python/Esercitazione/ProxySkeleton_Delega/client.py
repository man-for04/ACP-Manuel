#client.py
#lato client-> invocare proxy per accedere a servizi di rete

import sys
from proxy import Proxy

if __name__ == "__main__":
    IP = "localhost"
    try: #provo a ritirare i parametri da chiamata
        PORT = int(sys.argv[1])
        STRING = sys.argv[2]
        
    except (IndexError, TypeError):
        print("Errore parametri!")
        
    #parametri ok, contatto server
    print(f"[CLIENT] invio il server {IP}, {PORT} inviando <{STRING}>")
    
    proxy = Proxy(PORT)
    ris = proxy.inverti_stringa(STRING)
    
    print(f"{{CLIENT}} ho ottenuto risultato {ris}")
    