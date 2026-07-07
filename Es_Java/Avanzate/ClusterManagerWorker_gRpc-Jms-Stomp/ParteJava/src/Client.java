import java.util.Scanner;
import java.util.concurrent.TimeUnit;

import PackageTask.ClientThread;
import PackageTask.GestioneTaskGrpc;
import io.grpc.Channel;
import io.grpc.Grpc;
import io.grpc.InsecureChannelCredentials;
import io.grpc.ManagedChannel;

public class Client {
    private final GestioneTaskGrpc.GestioneTaskBlockingStub proxy;
    private final String[] task_types =new String[2];

    public Client(Channel channel){
        this.proxy = GestioneTaskGrpc.newBlockingStub(channel);
        this.task_types[0] = "gpu-bound";
        this.task_types[1] = "real-time";
    }

    public void run(){

        ClientThread[] threads = new ClientThread[5];

        for(int i=0;i<5;i++){
            threads[i] = new ClientThread(task_types, proxy);
            threads[i].start();
        }

        System.out.println("<Client> Thread avviati, aspetto la terminazione...");

        for(int i=0;i<5;i++){
            try {
                threads[i].join();
                System.out.println("Thread "+(i+1)+"/5 terminato");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args){
        
        Scanner input = new Scanner(System.in);
        System.out.println("Inserire porto desiderato: ");
        int port = input.nextInt();
        input.close();
        ManagedChannel channel = Grpc.newChannelBuilder("localhost:"+port, InsecureChannelCredentials.create()).build();

        Client client = new Client(channel);
        client.run();

        try {
            channel.shutdown().awaitTermination(5, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }
}
