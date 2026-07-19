import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;


import io.grpc.*;

public class ClusterManager {
    private Server server;

    public void serve(){

        ExecutorService executor = Executors.newCachedThreadPool();

        try {
            server = Grpc.newServerBuilderForPort(0, InsecureServerCredentials.create())
                    .executor(executor)
                    .addService(new GestioneTaskImpl())
                    .build()
                    .start();
        } catch (Exception e) {
            e.printStackTrace();
        }


        System.out.println("Server started on:"+ server.getPort());

        try {
            server.awaitTermination();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args){
        final ClusterManager2 cm = new ClusterManager2();
        cm.serve();
    }
}
