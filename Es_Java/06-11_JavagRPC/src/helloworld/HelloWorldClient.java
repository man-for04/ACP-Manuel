package helloworld;

//ci sono una serie di Import per i metodi usati

public class HelloWorldClient {

    private GreeterGrpc.GreeterBlockingStub greeter_stub;


    public HelloWorldClient(Channel channel){

        greeter_stub = GreeterGrpc.newBloc //.....
    }

    public void greet(String message){
        //oggetto request
        HelloRequest request = HelloRequest.newBuilder().setRequestMessage(message).build();
    }
    public static void main(String[] args){
        
        ManagedChannel channel = Grpc.newChannelBuilder("localhost: "+args[0], InsecureChannelCredentials.create()),build();
        HelloWorldClient client = new HelloWorldClient(channel);

        client.greet("Ciao sono giggino")

    }
    //fatti mandare resto del codice

}
