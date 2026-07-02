import stomp, time

class MioListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn
    
    def on_message(self, frame):
        print(f'Ho ricevuto messaggio {frame.body}')
        
if __name__ == "__main__":
    conn = stomp.Connection([('localhost', 61613)])
    
    conn.set_listener("", MioListener(conn=conn))
    
    conn.connect(wait = True, headers={'client-id':'cliente1'})
    print("Suscriber connesso!")
    
    conn.subscribe('/topic/miotopic',id=1, ack='auto', headers={'activemq.subscriptionName':'miaSubscription1'})
    
    time.sleep(40)
    conn.disconnect()