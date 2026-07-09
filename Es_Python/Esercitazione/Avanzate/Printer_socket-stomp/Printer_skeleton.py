from abc import ABC
from IPrinter import IPrinter

import socket

class Printer_skeleton(IPrinter, ABC):
    
    #definisce logica di comunicazione su socket TCP
    def run_skeleton(self):
        
        ssocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        ssocket.bind(('localhost', 0))
        info = ssocket.getsockname()
        print(f"Server in ascolto su {info[0]}, porto:{info[1]}")

        ssocket.listen()

        while True:
            conn, addr = ssocket.accept()
            
            from_user = str(conn.recv(1024).decode('utf-8'))
            print(f"--> Ricevuto dal client: {from_user}")
            
            try:
                #unpacking
                pathFile = str(from_user.split('#')[0])
                tipo = str(from_user.split('#')[1])
                
                
                self.print_function(pathFile, tipo)
        
            except (TypeError, IndexError):
                print("ERRORE nella lettura dei dati!")
            
            conn.close()
            print("conn chiusa")