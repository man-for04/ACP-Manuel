
from multiprocessing import Lock, Queue
from time import sleep

import stomp

from TicketsListener import TicketsListener
from MioStatsListener import MioStatsListener
from miaCoda import miaCoda

if __name__ == "__main__":
    conn_tickets = stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False)
    conn_stats = stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False)
    
    #Inizializzo la coda safe
    queue = Queue(20)
    lock = Lock()
    
    
    conn_tickets.set_listener("", TicketsListener(queue))
    conn_stats.set_listener("", MioStatsListener(queue, lock))
    
    conn_tickets.connect(wait=True)
    conn_stats.connect(wait=True)
    
    
    conn_tickets.subscribe(destination='/topic/tickets',id=1, ack="auto")
    conn_stats.subscribe(destination='/topic/stats',id=1, ack="auto")
    
    print("In attesa...\n")
    
    while(True):
        sleep(60)
    
