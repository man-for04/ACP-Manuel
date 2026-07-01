#serverImpl.py
#devo implementare buisness logic lato server e EREDITARE

from skeleton import Skeleton


class ServerImpl(Skeleton):
    def inverti_stringa(self, data):
        ret = data[::-1]
        return ret