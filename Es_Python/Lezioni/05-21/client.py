import requests


URL = "http://127.0.0.1:5000"

def testparam_req():
    
    querystring = {"key1" : "value1", "key2":"value2"}
    
    response = requests.get(URL + "/testparam", params=querystring)
    #response non è Response di Flask!! | BACK-END
    #Ma è response di requests | FRONT-END
    print(response)
    print(type(response))
    
    print("HEADER DELLA RISP")
    print(response.headers)
    print("BODY DELLA RISP (codificata in str) ",response.text)
    
    
def post_data1():
    
    payload="CIAOOOOO"
    response = requests.post(URL + "/data1", data=payload)
    print("RISPOSTA: ", response.text)
    
if __name__ == "__main__":
    
    #print("[CLIENT] invoking testparam")
    #attiva solo uno dei 2 se vuoi testarli per bene:
    testparam_req()
    
    post_data1()
    
    
    
#❓ha aggiunto parti di codice alla fine che non sei riuscito a scrivere, riveditele!