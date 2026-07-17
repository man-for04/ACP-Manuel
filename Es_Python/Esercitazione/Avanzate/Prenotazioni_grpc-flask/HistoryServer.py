from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():
    print("Hello")
    return 'Hello'


@app.post('/book_history')
def book_history():
    data = request.get_json()
    
    operation = data['operation']
    lab_number = data['lab_number']
    
    with open('history.txt', 'a') as out:
        out.write(f'{operation}-{lab_number}\n')
        out.flush()
        
    return 'ack'

if __name__ == "__main__":
    app.run(debug=True)
    print("Flask attivato!\n")