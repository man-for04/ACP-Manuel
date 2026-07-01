import socket


##in un loop fai la accept e poi receive/send

IP = '0.0.0.0' #così mi metto in ascolto su tutte le interfacce
PORT = 0 #default -- SO assegna in automatico

##istanza oggetto socket
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #ho creato uan socket ipv4 TCP -- non posso mettere in comuncazione socket different

##bind
s.bind((IP,PORT))
##listen
s.listen() #rischio di usare un porto già occcupato, meglio usare un porto che mi viene stampato!

#stampa delle info socket (pubblico l'avviso)
info = s.getsockname() #ritorna una lista
listening_address = info[0]
listening_port = info[1]
print("<s> server is listening on address", listening_address, " port: ", listening_port)

##accept
while True:
    conn, addr = s.accept() ## --> resto bloccato qui in loop finchè nessuno mi contatta⌛
                            ## conn è una seconda socket che viene usata per la comunicazione vera e propria
    print(f'<s> client, address {str(addr)}') #stampo la coppia IP/porto

    #ricevo dati
    data_from_client = conn.recv(4096)
    print(f'<s> Received data from client {data_from_client}')# normalmente recv dà i byte grezzi -> basta mettersi d'accordo sul formato di comunicazione con il comunicante
    print(f'<s> Received data from client {data_from_client.decode("utf-8")}')# è meglio farlo per andare sul sicuro

    toClient = "CIAO SONO IL SERVER..."
    conn.send(toClient.encode("utf-8"))

    print("<s> Chiudo connessione...")
    conn.close() #la "regola del pollice" è chiudere gli oggetti

##accetta la comunicazione e invia/ricevi
s.close()


### vedi strace e senti da 30 min in poi


#ls /proc
#strace python3 EsSocket_tcp_client.py 

# /proc/net/tcp è una struttura che mantiene tutte le associazioni socket/inode
# se metto grep "id dell'inode della socket trovato in ls -l /proc/PIDspecifico/fd"  /proc/net/tcp --> 
# ottengo varie informazioni come porto, stato della socket (es di listen)

#--> {l'ho sistemato bene sul quaderno}, nella foto vedi il caso della socket con il client connesso
