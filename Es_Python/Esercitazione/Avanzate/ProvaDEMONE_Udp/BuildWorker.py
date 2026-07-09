from flask import Flask, request
from werkzeug.exceptions import UnsupportedMediaType

app = Flask(__name__)

@app.route('/')
def hello():
    print("Benvenuto su flask")
    return 'ciao'

@app.post("/projects/<projectId>/test-runs")
def test_runs(projectId):
    #sia presente main.py nel progetto
    try:
        data = request.get_json()
        lista_file = data[projectId]
        
        if('main.py' in lista_file):
            print("main.py presente")
            return {'result':'pass'}
        else:
            return {'result':'fail'}
        
    except UnsupportedMediaType:
        return {'result':'fail'}


@app.post("/projects/<projectId>/style-checks")
def style_checks(projectId):
    
    #nome sia massimo 10 caratteri
    
    #sia presente README.md nei file
    try:
        data = request.get_json()
        lista_file = data[projectId]
        
        if('README.md' in lista_file) and (len(projectId) <= 10):
            print("ok")
            return {'result':'pass'}
        else:
            return {'result':'fail'}
    except UnsupportedMediaType:
        return {'result':'fail'}
    

if __name__ =="__main__":
    app.run()
    print("Server flask attivo")
