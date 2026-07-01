import sys, stomp, random
    
 #è il corrispondente del listener
 
if __name__ == "__main__":
 
    try:
            MSG = sys.argv[1]
    except IndexError:
            print("Please, specify MSG arg")
 
    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.connect(wait=True)

    conn.send('/topic/mytesttopic', MSG) #anche qui molto semplice, ma non ho queue -> ho TOPIC [publish/subscribe]
    print(f'Message: - {MSG} - sent!!!')
 
    conn.disconnect()
 