from concurrent import futures
import grpc
import order_management_pb2
import order_management_pb2_grpc

import logging #mon è obbligatorio per l'esame, è solo comodità
import uuid #per generare id univoci

class OrderManagementImpl(order_management_pb2_grpc.OrderManagementServicer):
    
    """
    un Order sarà del tipo
    ("12345678LELW":
            id: "12345678900",
            items: "oggetto 1"
            items: "oggetto 2"
            description: "oggetto 1 è un anello, oggetto 2 è ..."
            price: 50.00
            destination: "Napoli; Italia"
     
     ...       
    )
    
    """
    
    def __init__(self):
        self.orderDict = {}#oggetto interno alla nostra classe e modoficabile con metodi di classe(chiamate gRPC)

    def addOrder(self, request, context):
        
        id = uuid.uuid1() #genera ID per quest'ordine
        
        
        ##popola un oggetto order in accordo alla richiesta del client
        request.id = str(id)
        
        self.orderDict[request.id] = request
        
        logging.debug(f"[addOrder] aggiunto ordine con ID: {id}")
        
        response = order_management_pb2.StringMessage(message = str(id))
        
        return response
    
    def getOrder(self, request, context):
        
        id_to_search = request.message
        #order = self.orderDict[id_to_search]
        order=self.orderDict.get(id_to_search) #ritorna None se il valore associato alla chiave non c'è
        
        if order is not None:
            logging.debug(f"order found {order}")
            logging.debug(f"type(order) {type(order)}")
            return order #gia ho l'oggetto, l'ho già costruito!
        
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"L'ordine {id_to_search} non esiste") #non è obbligatorio, ma posso farlo e settare il contesto
            return order_management_pb2.Order()
        
    def searchOrders(self, request, context):
        #funzione di utitilià che restituisce lista di ordini a partire da dictionary quando c'è l'item
        
        matching_orders = self.searchInventory(request.message)
        
        for order in matching_orders:
            yield order     
        
    def searchInventory(self, item_name):
        #va usato item_name per fare ricerca nel dictionary | per tutte le key prendere i value e fare il match con item_name
        
        matching_orders = [] #lista di orders che contengono almeno un order name
        """
        for order_id,order in self.orderDict.items():
            for item in order.items: #è la lista di oggetti all'interno di items
                if item_name in item:
                    matching_orders.append(order)
                    break
        """
        if item_name in order.items:
            matching_orders.append(order)
            
        return matching_orders
    
    def processOrders(self, request_iterator, context):
        
        location_dict = {}
        
        for order in request_iterator:
            
            if order.destination not in location_dict.keys():
                location_dict[order.destination] = [order]
                
            else:
                location_dict[order.destination].append(order)    
                
        for key, values in location_dict.items():
            
            shipment_id = uuid.uuid1()
            shipment = order_management_pb2.CombinesShipment(id=str(shipment_id), status = "PROCESSED", orders = location_dict[key])
            
            yield shipment
            logging.debug("[OrderManagementServicer] processOrders: processed shipment" +str(shipment_id))

def serve():
    ##server è sempre nome, cambia solo nome della classe da implementare e nome del servizio che sto implementando
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),
                         options=(('grpc.so_reuseport',0),)) #se il server creato non è chiuso propriamente potrebbe bloccare l'indirizzo (così si evita), ma non è obbligatorio
    
    impl_object = OrderManagementImpl()
    order_management_pb2_grpc.add_OrderManagementServicer_to_server(impl_object,server)

    port = server.add_insecure_port("0.0.0.0:0")
    logging.debug(f"[SERVER] listening on localhost: {port}")
    
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    
    logging.basicConfig(format="%(asctime)s %(process)d %(message)s", level=logging.DEBUG) #timestamp+messaggio informativo + livello di severità da mostrare
    serve()