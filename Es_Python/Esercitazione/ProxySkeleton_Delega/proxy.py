#proxy.py
#PROXY lato client -> deve implementare la communication logic, ossia inviare richieste al server usando un rif a skeleton

from interface import SubjectInterface
import socket

class Proxy(SubjectInterface):
    def __init__(self, port):
        self.port = port
        
    def inverti_stringa(self, data):
        #devo creare comunicazione e inviare messaggio
        csocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        csocket.connect(("localhost", self.port))
        print("{PROXY} connesso al server!")
        
        csocket.send(data.encode("utf-8"))
        
        print("{PROXY} stringa inviata! ", data)
        
        ret = csocket.recv(4000).decode("utf-8")
        
        print("{PROXY} risposta ricevuta")
        csocket.close()
        return ret