from proxy import Proxy
import sys

if __name__ == '__main__':
    PORT = sys.argv[1]
    data = sys.argv[2]
    
    
    print(f'Mando richiesta di invertire {data} su localhost: {PORT}')
    
    p = Proxy(int(PORT))
    x= p.inverti_stringa(data)
    
    print("<CLIENT> stringa ricevuta: ", x)