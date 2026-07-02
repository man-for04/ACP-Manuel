from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    print(request.headers)
    return "<h1>Hello, %s!</h1>" %name

@app.route("/testparam")
def testparam():
    ##http://localhost:5000/testparam?key1=value1&key2=value2
    """
    body = request.body
    print("BODY: ", body)
    """
    querystring = request.args ##parametri passati dal ? in poi
    print("QUERYSTRING ", querystring)
    value1=querystring['key1']
    value2=querystring['key2']
    print(f"value1 {value1}  value2 {value2}") 
    
    return "ACK"


#@app.route(methods=["POST", "GET"], "/post1") #se voglio specificare serie di metodi leciti nella URI
#o volendo posso splittare lo stesso comando su più view function, non cambia nulla (è solo una questione di leggibilità)


"""
@app.post
@app.get
@app.delete
@app.put
@app.patch
così va a richiamare la rotta solo in presenza del metodo specificato (semplice)
"""

#curl -vv -d 'STRINGADIPROVA' "http://127.0.0.1:5000/data1"
@app.post("/data1")
def data1():
    
    data = request.get_data(as_text=True) #altrimenti non viene trattato come stringa, ma come flusso di byte
    print(data)
    return "ACK"

#fai chiamata con curl -vv --json -d '{"key1":"value1", "key2":"value2"}' "http://127.0.0.1:5000/post1"    -->passando json diventa automaticamente post, se non va sostuituisci a --json [ -X POST -H "Content-Type: application/json"  ]
#curl -vv -X POST -H "Content-Type: application/json" -d '{"key1":"value1", "key2":"value2"}' "http://127.0.0.1:5000/post1"

@app.post("/post1")
def post1():
    """
    voglio apssare nel poyload della post un   --> posso verificare se è scritto bene cercando su internet "JSON validator"
    {
        "key1" : "value1",
        "key2" : "value2"
    }
    """
    payload_json = request.get_json #sto supponendo che arrivi effettivamente un json, altrimenti fallisce
    print("PAYLOAD JSON")
    print(payload_json)
    
    return "ACK" #viene trattato automaticamente come stringa html in risposta verso il client (dal browser mostra ack nel body e basta)


#curl -vv http://127.0.0.1:5000/listusers
@app.get("/listusers")
def listusers():
    
    print("/listusers invoked")
    tutto_ok=False
    if tutto_ok:
        return ["gigi", "giggino", "gigione"] #interviene respose object che lo va a jsonificare
    else:
        return ("ERRORE LATO SERVER", 500)#posso ritornare uno status code

#💩

if __name__ == "__main__":
    app.run(debug=True)
