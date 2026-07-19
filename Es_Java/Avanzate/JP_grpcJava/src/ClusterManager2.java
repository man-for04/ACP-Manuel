import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import io.grpc.*;

public class ClusterManager2 {

    public static void main(String[] args){
        ExecutorService executor = Executors.newFixedThreadPool(10);
    
        try {
            Server server = Grpc.newServerBuilderForPort(0, InsecureServerCredentials.create()).executor(executor).addService(new TaskImpl()).build().start();

            System.out.println("Server listening on: "+server.getPort());


            server.awaitTermination();


        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }



}
