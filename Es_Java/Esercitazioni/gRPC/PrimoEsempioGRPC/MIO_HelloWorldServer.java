package PrimoEsempioGRPC;

import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import io.grpc.*;

public class MIO_HelloWorldServer {

    private Server server;

    public void serve(){
        ExecutorService executor = Executors.newFixedThreadPool(2);

        try {
            /*in python era 1. server = grpc.server(futures.ThreadPoolExecutor(10))
                            2.  servicer = new MioServicer()
                            3. ____.addServicerToServer(servicer, server)
                            4. server.add_insecure_port
                            5. server.start()
            */
            server = Grpc.newServerBuilderForPort(0, InsecureServerCredentials.create())
            .executor(executor)
            .addService(new MIO_GreeterImpl())
            .build()
            .start();

        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Server listening on " + server.getListenSockets() + "port: "+server.getPort());

        try {
            server.awaitTermination();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args){
        final MIO_HelloWorldServer mioServer = new MIO_HelloWorldServer();
        mioServer.serve();
    }
}
