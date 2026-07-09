from flask import Flask, request
from werkzeug.exceptions import UnsupportedMediaType

app = Flask(__name__)

@app.route('/')
def default():
    print("Benvenuto su flask!")
    return 'Ciao'

@app.post('/update_history')
def update_history():
    try:
        from_manager = request.get_json()
        
        op = from_manager['op']
        serial_number = from_manager['serial_number']
        
        to_write = f'{op}-{serial_number}'
        
        print(f"-->Ricevuto da manager: {to_write}")
        
        with open('history.txt', 'a') as out:
            out.write(to_write+'\n')
            out.flush()
            print("Scritto")
            
        return 'ack'
    
    except UnsupportedMediaType as e:
        print("ERRORE! Json non valido: ", e)
        return ('error', 400)
    
if __name__ =="__main__":
    app.run(host='127.0.0.1', debug=True)
    print("Flask partito!")