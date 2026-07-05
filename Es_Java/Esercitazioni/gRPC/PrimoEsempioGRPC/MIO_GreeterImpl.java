package PrimoEsempioGRPC;

import io.grpc.stub.StreamObserver;

public class MIO_GreeterImpl extends GreeterGrpc.GreeterImplBase{

    @Override
    public void sayHello(HelloRequest request, StreamObserver<HelloReply> responseObserver) {
        //Implementazione del servizio
        System.out.println("Servizio sayHello invocato, client ha inviato: "+request.getName());
        
        HelloReply risposta = HelloReply.newBuilder().setMessage("Ciao "+request.getName()).build(); //Costruire un messaggio con builder

        System.out.println("Invio risposta" + risposta +" al client...");

        //Inviare risposta con pattern observer
        responseObserver.onNext(risposta);
        responseObserver.onCompleted();
    }
    
}
