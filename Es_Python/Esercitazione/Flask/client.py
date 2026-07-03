#client che, mediante libreria requests, potrà inviare da codice richieste al server flask helloworld.py
import requests

def print_response(response : requests.Response):
    
    print("Encoding: ", response.encoding)
    print("Status code:", response.status_code)
    print("URL:", response.url)
    print("Server Header:", response.headers['Server'])
    print("Headers:", response.headers)
    print("Content:", response.content)
    print("Text", response.text)
    
    try:
        print("JSON: ", response.json())
    except requests.exceptions.JSONDecodeError:
        print("FORMATO NON JSON!!!!")
        
    print()
    
    
#HEAD
print("--> HEAD")
r = requests.head('http://localhost:5000/')
print_response(r)

print("-->GET")
parametri = {'key1':'Forza',
             'key2': ['Napoli', 'Sturm']}
r = requests.get('http://localhost:5000/testparam', params=parametri)
print_response(r)

print('-->POST')
parametro_json = {'campo1':'Manuel', 
                  'campo2': 21}
r = requests.post('http://localhost:5000/json', json=parametro_json)
print_response(r)

print("-->POST")
dati = 'ciaoooo'
r = requests.post('http://localhost:5000/data', data=dati)
print_response(r)

print("-->GET")
r = requests.get('http://localhost:5000/me')
print_response(r)

print("-->GET")
r = requests.get('http://localhost:5000/users')
print_response(r)

print("-->GET")
r = requests.get('http://localhost:5000/user_adv/ciao')
print_response(r)