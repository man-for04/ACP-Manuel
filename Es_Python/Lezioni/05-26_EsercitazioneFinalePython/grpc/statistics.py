import grpc
import statistics_pb2
import statistics_pb2_grpc
import pymongo

from concurrent import futures

def get_database():
    mongo_client = pymongo.MongoClient("localhost", 27017)
    return mongo_client['sensors_database']


class StatisticsServicer(statistics_pb2_grpc.StatisticsManagerServicer):
    
    def __init__(self, database):
        self.database = database

    def getSensors(self, request, context):
        
        sensors_collection = self.database['sensors']
        
        results_cursor = sensors_collection.find(())
        
"""
message Sensor {

    int64 sensor_id = 1; //consiglio: usa lo stesso nome che hai usato in flask! Così non impazzisci
    string data_type = 2;
}
"""
        
        for sensor in results_cursor:
            
            s_id = sensor['sensor_id']
            d_type = sensor['data_type']
            yield statistics_pb2.Sensor(sensor_id = s_id, data_type = d_type)
        
        
        

if __name__ == "__main__":
    
    client_mongodb = get_database()
    
    server: Server = grpc.server(thread_pool=futures.ThreadPoolExecutor(max_workers=10))
    
    ##crea l'oggetto servicer e aggiungilo al server
    
    s: Any = StatisticsServicer()
    statistics_pb2_grpc.add_StatisticsManagerServicer_to_server(servicer=s, server)
    
    server.add_insecure_port(address="::0")
    server.start()
    
    server-wait_for_termination()