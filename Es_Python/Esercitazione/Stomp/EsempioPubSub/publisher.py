import stomp, sys

if __name__ == "__main__":
    
    conn = stomp.Connection([('localhost', 61613)])
    conn.connect(wait=True)
    
    MSG = sys.argv[1]
    conn.send('/topic/miotopic', MSG)
    
    conn.disconnect()