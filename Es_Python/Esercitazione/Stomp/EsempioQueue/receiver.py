import stomp, time

class MioListener(stomp.ConnectionListener):
    
    def __init__(self, conn):
        self.conn = conn
    
    def on_message(self, frame):
        print(f"Ho ricevuto messaggio {frame.body}")
        
if __name__=="__main__":
    conn = stomp.Connection([('127.0.0.1', 61613)])
    
    conn.set_listener("", MioListener(conn=conn))
    
    conn.connect(wait=True)
    
    conn.subscribe('/queue/miacoda1', id=1, ack='auto')
    
    print(f"Receiver avviato! Sono pronto a ricevere su {conn.is_connected()}")
    
    time.sleep(50)
    
    conn.disconnect()