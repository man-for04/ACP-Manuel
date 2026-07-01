#serverImpl.py
#deve implementare la buisness logic del server e basta.

from interface import SubjectInterface

class ServerImpl(SubjectInterface):
    def inverti_stringa(self, data):
        #deve ritornare stringa invertita
        return data[::-1]