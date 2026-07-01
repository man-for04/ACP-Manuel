
##PUBLISHER DURABILE -> Di per sè come un receiver (eredita on_message), usa un TOPIC + impostazioni relative a DURABLE

import time
import stomp
    

class MyListener(stomp.ConnectionListener):
    
    def __init__(self, conn):
        self.conn = conn

    def on_message(self, frame):
        print('received a message')
        print('text: "%s"' % frame.body)
        print('headers: "%s"' % frame.headers)
        print('cmd: "%s"' % frame.cmd)

if __name__ == "__main__":
    
    conn = stomp.Connection([('127.0.0.1', 61613)])

    conn.set_listener('', MyListener(conn))

    conn.connect(wait=True, headers = {"client-id":"IDtestsub_durable_queue"})#header per durabilità

    print("Creating a DURABLE SUBSCRIBER...")

    conn.subscribe(destination='/topic/mytesttopic', 
    			id=1, 
    			ack='auto', 
    			persistent=True, 
    			headers = {"activemq.subscriptionName":"DURABLESUB_NAME_queue"})   #a che serve quindi il subscriber durabile? Va a recuperare anche messaggi che 
                                                                                    #sono stati inviati mentre non era attivo! 
                                                                                    #Per provarlo basta mandare tot messaggi con SUBSCRIBER SPENTO. Appena lo attivo, li recupera tutti

    print('DURABLE SUBSCRIBER waiting for messages...')

    time.sleep(60)

    conn.disconnect()