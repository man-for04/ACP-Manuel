#Statistics.py
#questo è il server grpc

import statistiche_pb2
import statistiche_pb2_grpc
import grpc
import pymongo
import concurrent.futures


def get_database():
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = client['dbSensori']
    return db


class StatisticheServicerImpl(statistiche_pb2_grpc.StatisticheServicer):
    def getSensors(self, request, context):
        print("<SERVER> getSensors attivata!")
        db = get_database()
        collection = db['sensors']
        print("<Statistics> Vado a recuperare i dati dei sensori...")
        
        sensors = collection.find({})
        #print(f'Gruppo di sensori trovati: {sensors}')
        for sensore in sensors:
            try:
                print(sensore)
                id = sensore['_id']
                data_type = sensore['data_type']
            except Exception as e:
                print("Qualcosa è andato storto nel formato del sensore: ",print(sensore), print(e))
                
            else:
                print(f"Recuperato sensore {id}, {data_type}. Procedo a invio...")
                yield statistiche_pb2.Sensor(id=id, data_type=data_type)
        
        
        
    def getMean(self, request, context):
        print("<SERVER> getMean attivata!")
        id = request.id
        dt = request.data_type
        db = get_database()
        
        if dt=='temp':
            media = float(0)
            contatore = float(0)
            collection = db['temp_data']
            misurazioni = collection.find({'sensor_id':id})
            
            for misurazione in misurazioni:
                try:
                    media += misurazione['data']
                    contatore+=1
                except Exception:
                    print(f"Errore! Sensore {id} non trovato")
            
            media = media/contatore
            
        elif dt == 'press':
            media = float(0)
            contatore = float(0)
            collection = db['press_data']
            misurazioni = collection.find({'sensor_id':id})
            
            for misurazione in misurazioni:
                try:
                    media += misurazione['data']
                    contatore+=1
                except Exception:
                    print(f"Errore! Sensore {id} non trovato")
            
            media = media/contatore
            
        else:
            print("Errore! Tipo di sensore non riconosciuto!")
            media = -1
            
        return statistiche_pb2.StringMessage(media=media)
    
    
if __name__ == "__main__":
    
    servicer = StatisticheServicerImpl()
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    statistiche_pb2_grpc.add_StatisticheServicer_to_server(servicer, server)
    
    port = server.add_insecure_port("0.0.0.0:0")
    print("Server statistics listening on localhost, port: ", port)
    
    server.start()
    
    server.wait_for_termination()