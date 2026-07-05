package PrimoEsempioGRPC;

import java.util.concurrent.TimeUnit;

import io.grpc.*;

public class MIO_HelloWorldClient {

    private final GreeterGrpc.GreeterBlockingStub proxy;

    public MIO_HelloWorldClient(Channel channel){
        
        proxy = GreeterGrpc.newBlockingStub(channel);
    }

    public void greet(String nome){
        //Comportamento del client

        
        HelloRequest richiesta = HelloRequest.newBuilder().setName(nome).build();
        HelloReply risposta;

        System.out.println("Sono il client, invio a Server messaggio..." + richiesta);
        risposta=proxy.sayHello(richiesta);
        System.out.println("Risposta ottenuta: "+risposta.getMessage());
    }

    public static void main (String[] args)throws Exception{
        ManagedChannel channel = Grpc.newChannelBuilder("localhost:"+args[0], InsecureChannelCredentials.create()).build();

        try{
            MIO_HelloWorldClient mioClient = new MIO_HelloWorldClient(channel);
            mioClient.greet(args[1]);
        }
        finally{
            channel.shutdown().awaitTermination(5, TimeUnit.SECONDS);
        }
    }
}
