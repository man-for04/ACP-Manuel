package ciaoooo;

import java.util.concurrent.TimeUnit;

import ciaoooo.Salutoni.stringMessage;
import io.grpc.*;

public class MioClient {

    ciaoooo.GreeterGrpc.GreeterBlockingStub proxy;

    public MioClient(Channel channel){
        proxy = GreeterGrpc.newBlockingStub(channel);
    }

    public void start(){

        stringMessage to_server = stringMessage.newBuilder().setContenuto("mario").build();

        stringMessage from_server = proxy.sayHello(to_server);

        System.out.println("Ricevuto: "+ from_server);
    }

    public static void main(String args[]){

        int porto = Integer.parseInt(args[0]);

        ManagedChannel channel = Grpc.newChannelBuilderForAddress("localhost", porto, InsecureChannelCredentials.create()).build();


        MioClient client = new MioClient(channel);
        client.start();

        try {
            channel.shutdownNow().awaitTermination(5, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
