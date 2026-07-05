package PrimoEsempioGRPC;
import io.grpc.*;
import io.grpc.stub.StreamObserver;

public class Implementatore extends GreeterGrpc.GreeterImplBase{

    @Override
    public void sayHello(HelloRequest request, StreamObserver<HelloReply> responseObserver) {

        System.out.println("Ricevuto messaggio "+request.getName());
        HelloReply reply = HelloReply.newBuilder().setMessage("a").build();

        responseObserver.onNext(reply);
        responseObserver.onCompleted();
    }

}
