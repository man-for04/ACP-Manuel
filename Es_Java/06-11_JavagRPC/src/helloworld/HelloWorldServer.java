package helloworld;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import io.grpc.Grpc; //mi oermette di creare Server (builder)

public class HelloWorldServer {
    
    private Server server;

    private void start(){
        //devo creare il pull di Executor
        ExecutorService executor = Executors.newFixedThreadPool(10);
        //per creare nuovo Server mi serve per forza pattern Builder
        int port = 0;
        /* 
        server = Grpc.newServerBuilderForPort(port, InsecureServerCredentials.create());
        */
       ServerBuilder<?> serverBuilder = Grpc.newServerBuilderForPort(InsecureServerCredentials.create());

        serverBuilder.executor(executor);
        serverBuilder.addService(new GreeterImpl());
        server = serverBuilder.build();
        server.start(); //andrà gestita eccezione con try-catch




        System.out.println();
        server.awaitTermination(); //sempre con try-catch, a causa di Thread (InterruptException)

        System.out.println("Server avviato localhost:");

    }

    public static void main(String[] args){
        HelloWorldServer hello_server = new HelloWorldServer();
        hello_server.start());
    }
}
