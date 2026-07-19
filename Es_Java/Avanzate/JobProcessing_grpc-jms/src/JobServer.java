import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import io.grpc.Grpc;
import io.grpc.InsecureServerCredentials;
import io.grpc.Server;

public class JobServer {
    
    public static void main(String[] args){

        ExecutorService executors = Executors.newFixedThreadPool(10);

        try {
            Server server = Grpc.newServerBuilderForPort(0, InsecureServerCredentials.create()).addService(new JobImpl()).executor(executors).build().start();

            System.out.println("Server listening on: "+server.getPort());

            server.awaitTermination();
            
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }

    }
}
