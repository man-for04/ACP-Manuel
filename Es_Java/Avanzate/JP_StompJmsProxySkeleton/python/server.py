from multiprocessing import Queue

from serverImpl import serverImpl


if __name__ == "__main__":
    queue = Queue(5)  
    port = 0
    
    service = serverImpl(port, queue)
    
    service.run_skeleton()