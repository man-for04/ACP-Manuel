#Dashboard.py

import statistiche_pb2
import statistiche_pb2_grpc
import grpc
import sys

if __name__ == "__main__":
    with (grpc.insecure_channel("localhost:"+sys.argv[1])) as channel:
        proxy = statistiche_pb2_grpc.StatisticheStub(channel)
        
        print("Richiedo i sensori: ")
        msg = statistiche_pb2.Empty()
        sensori = proxy.getSensors(msg)
        
        for sensor in sensori:
            print(f'\n__________________\nSensore <{sensor}>: ')
            id = sensor.id
            data_type = sensor.data_type
            media = proxy.getMean(statistiche_pb2.MeanRequest(id=id, data_type=data_type))
            print("Media: ", media)