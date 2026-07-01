from serverInterface import ServerInterface

#deve solo implementare business logic, al resto ci pensa serverSkeleton

class ServerImpl(ServerInterface):
    """
    nessun parametro particolare
    """
    def inverti_stringa(self, data):
        print("<server_impl> inverti_stringa() invocato")
        r = data[::-1]
        
        return r