package PrimoEsempioGRPC;


import java.util.concurrent.TimeUnit;

import io.grpc.*;

public class client {
    private final GreeterGrpc.GreeterBlockingStub proxy;

    public client(Channel channel) {
        this.proxy = GreeterGrpc.newBlockingStub(channel);
    }


    public void run(){
        //costruisce e riceve messaggi
        HelloRequest richiesta = HelloRequest.newBuilder().setName("a").build();
        HelloReply risposta = proxy.sayHello(richiesta);
    }

    public static void main(String[] args){
        ManagedChannel channel = Grpc.newChannelBuilder("localhost:1234", InsecureChannelCredentials.create()).build();

        client clientee = new client(channel);

        clientee.run();

        try {
            channel.shutdown().awaitTermination(5, TimeUnit.SECONDS); //⭕⭕⭕⭕
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    
    
}
