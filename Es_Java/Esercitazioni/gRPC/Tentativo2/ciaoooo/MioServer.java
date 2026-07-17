package ciaoooo;

import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import io.grpc.*;

public class MioServer {

    private Server server;

    public void serve() throws IOException, InterruptedException{

        int porto = 0;

        ExecutorService executor = Executors.newFixedThreadPool(2);
        server =Grpc.newServerBuilderForPort(porto, InsecureServerCredentials.create()).executor(executor).addService(new GreeterImpl()).build().start();

        System.out.println("Server listening on: "+server.getPort());
        
        server.awaitTermination();

    }

    public static void main(String args[]){

        MioServer mioserver = new MioServer();
        try {
            mioserver.serve();
        } catch (IOException | InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
