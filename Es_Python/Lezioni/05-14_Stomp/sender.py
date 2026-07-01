#semplice, creo la connessione e invio il messaggio, poi disconnetto
import stomp
import time

if __name__=="__main__":
    
    conn = stomp.Connection([("127.0.0.1", 61613)])
    
    conn.connect(wait=True) #per attenedere che la connessione sia completata || in java NON dovrò mettere attesa attiva (è gestita automaticamente)
    
    ##invio
    
    conn.send("/queue/miacoda", "CIAO SONO A") #attenzione a non confondere tra topic e queue!
    
    print(f'[SENDER] inviato CIAO A')
    
    conn.disconnect()
    
    #🛠️ Se non funziona -> studente@studente:~/apache-activemq-5.16.6/bin$ ./activemq console
    #ossia spostati in quella cartella e lancia il comando per attivare il server