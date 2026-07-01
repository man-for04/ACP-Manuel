package helloworld;

public class GreeterImpl extends GreeterGrpc.GreeterImplBase{

    @Override
    public void sayHello(HelloRequest request, StreamObserver ) {
        //...
    }


}
