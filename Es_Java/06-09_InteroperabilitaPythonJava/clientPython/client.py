#1. COSA DA FARE -> si scrive in 5 minuti

import stomp

class ClientListener(stomp.ConnectionListener):
    
    def on_message(self, message):
        
        print(f"[CLIENT] ricevuto messaggio ", message)



if __name__ == "__main__":
    
    conn = stomp.Connection([("127.0.0.1", 61613)],
                                auto_content_length=False)# il porto sta sia nella documentazione che nel readME dell'esame
                                                #False va messo per consentire textMessage, altrimenti non funziona!
    
    conn.set_listener('', ClientListener())
    conn.connect()
    
    #mettiti in ricezione asincrona su response
    conn.subscribe(destination='/queue/response', id=1, ack='auto') #⭕sulla coda posso passare solo stringhe, attento!
    
    for i in range(10):
        if(i%2 == 0):
            #deposita
            message_to_send = "deposita-" +i
            
        else:
            #preleva
            message_to_send = "preleva"
            
        conn.send(destination='/queue/request', headers={"reply-to":"/queue/response"}) #headers sarà un dict (nella documentazione ActiveMQ lo chiama una 'map')
        
        print(f"[CLIENT] messaggio {message_to_send} inviato...")
        
    while True:
        time.sleep(60)
        
    