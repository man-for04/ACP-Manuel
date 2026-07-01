#avviare lo skeleton e passare il porto

from serverImpl import ServerImpl

if __name__ == "__main__":
    print("Ciao sono il server")
    PORT = 0
    
    si = ServerImpl(PORT)
    si.run_skeleton()