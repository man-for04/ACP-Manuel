
import java.util.concurrent.TimeUnit;

import io.grpc.*;
import mioPackage.TaskManagementGrpc;
import mioPackage.TaskManagementGrpc.TaskManagementBlockingStub;


public class Client2 {

    private final TaskManagementBlockingStub stub;

    public Client2(Channel channel){
        stub = TaskManagementGrpc.newBlockingStub(channel);
    }

    public void greet(){
        //Il comportamento
        ClientThread[] threads= new ClientThread[5];

        for(int i=0;i<5;i++){
            threads[i] = new ClientThread(stub);
            threads[i].start();
        }

        for(int j=0;j<5;j++){
            try {
                threads[j].join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args){

        ManagedChannel channel = Grpc.newChannelBuilder("localhost:"+args[0], InsecureChannelCredentials.create()).build();

        Client2 mioClient = new Client2(channel);

        mioClient.greet();

        try {
            channel.shutdownNow().awaitTermination(5, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        };


    }
}
