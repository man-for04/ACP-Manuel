import stomp, sys

if __name__ == "__main__":
    conn = stomp.Connection([('localhost', 61613)])
    conn.connect(wait=True)
    
    try:
        MSG = sys.argv[1]
        
    except IndexError:
        print("Errore parametri ingresso!")
        
    print("Per testare transazione, stampo 3 messaggi! Se MSG è a, fa abort")
    
    t_id = conn.begin()
    conn.send('/queue/miacoda1', 'Ciaooo', transaction=t_id)
    conn.send('/queue/miacoda1', 'Hellooo', transaction=t_id)
    conn.send(destination='/queue/miacoda1', body=MSG, transaction= t_id)
    
    if(MSG == 'a'):
        conn.abort(t_id)
        print("Abortito")
    else:
        conn.commit(t_id)
        print("Transazione ok")
    
    print(f'Messaggio {MSG} inviato')
    
    conn.disconnect()