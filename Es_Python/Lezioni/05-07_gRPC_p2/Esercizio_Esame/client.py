import grpc
import order_management_pb2
import order_management_pb2_grpc

import logging, sys

def generate_orders_for_shipment():

    ordine1 = order_management_pb2.Order(id = "0001", price=2332, items=['item - A', 'Item - B'], description = "Updated desc",destination = "San Jose, CA")
    #(modifica gli altri 2 ordini per renderli diversi)
    ordine2 = order_management_pb2.Order(id = "0001", price=2332, items=['item - A', 'Item - B'], description = "Updated desc",destination = "San Jose, CA")
    ordine3 = order_management_pb2.Order(id = "0001", price=2332, items=['item - A', 'Item - B'], description = "Updated desc",destination = "San Jose, CA")

    order_list = [ordine1, ordine2, ordine3]
    for order in order_list:
        yield order


def client(port):
    
    with grpc.insecure_channel("localhost:" +port) as channel:
        
        ##creo stub client
        stub = order_management_pb2_grpc.OrderManagementStub(channel) #prende canale e sul canale aggiunge attributo all'interno della classe a cui asssegna un handler associato a una chimaata unary-unary
        
        order1 = order_management_pb2.Order( #campi possono anche non essere specificati (saranno vuoti)
            
                items=["oggetto1", "oggetto2"],
                description="descrizione semplice 1", 
                price=50.00,
                destination="Napoli"
            )#bisogna passare per il costruttore di messaggio, non posso usare banalmente un dizionario
        
        order2 = order_management_pb2.Order( #campi possono anche non essere specificati (saranno vuoti)
            
                items=["oggetto1", "oggetto3"],
                description="descrizione semplice 2", 
                price=10.00,
                destination="Pollena Trocchia"
            )
        
        
        id_order1 = stub.addOrder(order1)
        print(f"[CLIENT] addOrder({order1}) invocata, id order {id_order1}")
        
        print(f"[CLIENT] getOrder invoked on {id_order1}")
        order1_get = stub.getOrder(id_order1)
        print(f"[CLIENT] getOrder returns {order1_get}")
        
        order_id_to_get = order_management_pb2.StringMessage("000000001")
        print(f"[CLIENT] getOrder invocata su {order_id_to_get}") ##se avessi messo direttamente stringa avrebbe dato errore
        order2_get = stub.getOrder(order_id_to_get) #richiedo quello che ho appena aggiunto passando l'id ottenuto dal server
        print(f"[CLIENT] getOrder restituisce: {order2_get}")
        
        
        print(f"[CLIENT] addOrder{order2}")
        id_order2= stub.addOrder(order2)
        print(f"[CLIENT] addOrder invocata, id order {id_order2}")
        
        
        print("###############")
        print("[CLIENT] searchOrders invoked for oggetto1")
        
        test_orders1 = stub.searchOrders(order_management_pb2.StringMessage(message="oggetto1"))
        for order in test_orders1:
            
            print(f"[CLIENT] ordine {order} contiene oggetto1")
        
        print("###############")
        print("[CLIENT] searchOrders invoked for oggetto2")
        test_orders2 = stub.searchOrders(order_management_pb2.StringMessage(message="oggetto2"))
        """
        message Order {
        string id = 1;
        repeated string items = 2;
        string description = 3;
        string price = 4;
        string destination = 5; 
        }
    """
    
    
    ### 4) Creare generatore per le richieste del client
    client_generator = generate_orders_for_shipment()
    
    shipments = processOrders(client_generator)
    for shipment in shipments: #ovviamente se fosse UNARIA nella risposta non farei questa iterazione
        print(f"[CLIENT] shipment {shipment}") 

if __name__ == "__main__":
    
    port = sys.argv[1]
    client(port)