import socket, sys, time

def client(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("<c> Invio richiesta connessione a localhost e porto specificato come argv")
    s.connect(("localhost", port))

    #send prima al server
    message = "CIAO SONO IL CLIENT...."
    s.send(message.encode("utf-8"))

    #altro???
    print("<c> messaggio inviato al server")

    ##recv del server

    data = s.recv(4096)
    print(f'<c> Dato ricevuto dal server {data.decode("utf-8")}')

    time.sleep(300)
    print("<c> Chiudo connessione...")
    s.close()

if __name__ == "__main__":

    port = int(sys.argv[1])
    client(port)