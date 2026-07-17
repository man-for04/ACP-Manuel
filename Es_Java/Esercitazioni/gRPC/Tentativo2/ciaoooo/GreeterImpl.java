package ciaoooo;

import ciaoooo.Salutoni.stringMessage;
import io.grpc.stub.StreamObserver;

public class GreeterImpl extends ciaoooo.GreeterGrpc.GreeterImplBase{

    @Override
    public void sayHello(stringMessage request, StreamObserver<stringMessage> responseObserver) {
        
        String from_client = request.getContenuto();

        stringMessage reply = stringMessage.newBuilder().setContenuto("ciao "+from_client).build();

        responseObserver.onNext(reply);
        responseObserver.onCompleted();
    }

}
