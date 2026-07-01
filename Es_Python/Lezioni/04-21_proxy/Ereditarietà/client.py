#client deve solo richiedere il servizio tramite il proxy
from proxy import Proxy
import sys #good (gùt)


if __name__ == "__main__":
    
    try:
        PORT = sys.argv[1]
        MESSAGE = sys.argv[2]
    
    except IndexError:
        print("Errore")
        
    print(f'Mando richiesta di invertire {MESSAGE} su localhost {PORT}')
    
    
    ##istanzia proxy e invoca metodo remoto
    proxy = Proxy(int(PORT)) #NON passare messaggio, ma tutto ciò che serve per la comunicazione in rete
    stringa_invertita = proxy.inverti_stringa(MESSAGE)
    print('Stringa invertita: ', stringa_invertita)