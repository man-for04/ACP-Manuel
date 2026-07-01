import stomp
import time

#non cambia nulla
class MyListener(stomp.ConnectionListener):
    
    def __init__(self, conn):
        self.conn=conn
        
    def on_message(self, frame):
        print("msg ricevuto")
        print('text: "%s"' %frame.body)
        print('headers:  "%s"' %frame.headers)
        print('cmd: "%s"' %frame.cmd)



if __name__ == "__main__":
    conn = stomp.Connection([("127.0.0.1", 61613)])
    
    #devo specificare listener e sottoscrivere
    conn.set_listener("", MyListener(conn))
    
    conn.connect(wait=True)
    
    conn.subscribe("/queue/miacoda", id="1", ack="auto")
    
    time.sleep(60)
    
    conn.disconnect()