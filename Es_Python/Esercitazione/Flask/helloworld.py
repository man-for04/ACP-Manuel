
import random

from flask import Flask, render_template, request, make_response
import os

from werkzeug.exceptions import RequestTimeout

#template_dir = os.path.abspath('./templates/')

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, world!</h1>"

@app.route("/user/<name1>")
def user(name1):
    
    return render_template('user.html', name=name1)


@app.route("/testparam")
def testparam():
    querystring = request.args
    print("QUERYSTRING ", querystring)
    val1 = querystring['key1']
    val2 = querystring['key2']
    print(f'val1: {val1}')
    print(f'val2: {val2}')
    
    return querystring


@app.route('/user_adv/<name>')
def user_adv(name):
    if name == 'pippo':
        return render_template('user_adv.html', name=name, elements=['String', 10, {'key':'value'}])
    else:
        return render_template('user_adv.html')
    
    
@app.route('/user_agent')  # pyright: ignore[reportArgumentType]
def user_agent():
    user_agent=request.headers.get('User-Agent')
    return user_agent

@app.post('/data')
def data():
    data = request.get_data(as_text=True)
    print("hai inviato: ",data)
    argomenti = request.args.get
    print("args: ", argomenti)
    return data


@app.post('/json')  #curl --json '{"text":"prova"}' http://localhost:5000/json gli mando il json e mi restituisce il json stesso
def json():
    json = request.get_json()
    print("hai inviato: ", json)
    return json


@app.route('/print', methods=['GET', 'POST'])
def print2():
    if(request.method=='GET'):
        return 'This is a GET'
    else:
        return 'This is a POST'
    
@app.get('/print2')
def print_get():
    return 'This is a GET'

@app.post('/print2')
def print_post():
    return 'This is a POST'

@app.route('/me')
def me_api():
    user = {
        "username" : "Manuel",
        "eta" : 21
    }
    print(f"tipo: {type(user)}")
    return user

@app.route('/error')
def error():
    return ('Bad requesttt', 400)

@app.route('/error_header')
def error2():
    headers = {'mioHeader' : 'Ciao'}
    return ('MessaggioErrore', 400, headers)

@app.route('/make')
def make():
    print("Eccomi")
    ret = make_response('Questo è un cookie!')
    ret.set_cookie('aaaa')
    return ret


def get_all_users():

    usernames = ['pippo', 'pluto', 'pippozzo', 'plutozzo']
    users = []

    for usename in usernames:

        users.append({'username': usernames.pop(), 'age': random.randint(18, 99)})

    return users


@app.route('/users')
def users_api():
    users = get_all_users() #ritorna lista
    return users


if __name__=="__main__":
    app.run(debug=True)