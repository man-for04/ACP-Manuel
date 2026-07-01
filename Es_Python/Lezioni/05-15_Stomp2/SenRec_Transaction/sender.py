import stomp
import time
import random

if __name__=="__main__":
    
    conn = stomp.Connection([("127.0.0.1", 61613)])
    
    conn.connect(wait=True)
    
    ##invio
    #voglio iniziare una transazione di m messaggi con problemi lato server (simulo eccezione che non mi fa fare la send) :
    id_transazione = conn.begin()
    """
    conn.send("/queue/miacoda", "CIAO SONO A", transaction = id_transazione)
    conn.send("/queue/miacoda", "CIAO SONO B", transaction = id_transazione)
    conn.send("/queue/miacoda", "CIAO SONO C", transaction = id_transazione)
    conn.abort()
    
    conn.commit(id_transazione)
    print(f'[SENDER] inviato CIAO A')
    """
    try:
        
        for i in range(3):
            value = random.randint(0,1)
            if(value == 0):
                raise IOError("errore di I/O")
            conn.send("/queue/miacoda", "CIAO SONO X " +str(i), transaction=id_transazione) ##📝servirà per poter effettuare dei controlli, lo chiede all'orale
            
    except IOError:
        conn.abort(id_transazione)
        print("[SENDER] Transazione abortita")
        
    else:
        conn.commit(id_transazione)
        print("[SENDER] Transazione eseguita")
    
    #il broker è Single Point of Failure (o meglio, il nodo che lo ospita lo è)
    #se invio 1 milione di messaggi, il borker dovrà accumularli finchè non arriva qualcuno a ritirarli! Aumenta ovviamente complessità spaziale
    conn.disconnect()