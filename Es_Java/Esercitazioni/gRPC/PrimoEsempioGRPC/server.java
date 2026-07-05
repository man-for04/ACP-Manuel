package PrimoEsempioGRPC;
import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import io.grpc.*;

public class server {

    private Server server;

    public void serve(){
        ExecutorService executor = Executors.newFixedThreadPool(2);

        try {
            server = Grpc.newServerBuilderForPort(0, InsecureServerCredentials.create())
            .executor(executor)
            .addService(new Implementatore())
            .build()
            .start();
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Server partito su "+server.getPort());

        try {
            server.awaitTermination();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args){
        final server sv = new server();
        sv.serve();
    }
}
