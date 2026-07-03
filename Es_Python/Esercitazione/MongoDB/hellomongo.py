import pymongo

client = pymongo.MongoClient("localhost", 27017)

db = client['test-database']

collection = db['test-collection']

doc1 = {'nome':'Manuel',
        'cognome': 'Fornataro',
        'eta': 21,
        'luogo di nascita': 'Napoli'}

doc2 = {'nome':'Alex', 
        'cognome':'Fornataro',
        'eta': 18, 
        'luogo di nascita':'Napoli'}

doc3 = {
    'nome':'Doris', 
        'cognome':'Riegelnegg',
        'eta': 57, 
        'luogo di nascita':'Graz'
}

"""
collection.insert_one(doc1)
collection.insert_many([doc2, doc3])
"""
#print(collection.update_one({"nome":"Manuel"}, {"$set":{"luogo di nascita":"NAPOLI"}}))

x=collection.find({"luogo di nascita":{"$in" : ["Graz", "Napoli"]}}, )
print(type(x))
for r in x:
    print(r)





