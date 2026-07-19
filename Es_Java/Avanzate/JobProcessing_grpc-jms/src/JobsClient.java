import java.util.concurrent.TimeUnit;

import io.grpc.*;
import mioPackage.JobsGrpc;
import mioPackage.IJobUser.*;
import mioPackage.JobsGrpc.JobsBlockingStub;
import java.util.Random;

public class JobsClient {

    //private String[] tipiProcessing = {"cpu-intensive", "gpu-intensive"};
    //Ho dovuto cambiare il nome per evitare conflitti!
    private JobsBlockingStub stub;

    public JobsClient(Channel channel){
        //porto?
        this.stub = JobsGrpc.newBlockingStub(channel);
    }

    public void greet(int tipoProcessing, String nomeFile){

        //genera 5 richieste con attesa 2 sec,
        String nomeJob;

        Random rand = new Random();

        for(int i=0;i<5;i++){
            nomeJob = "job"+rand.nextInt(0, 101);
            
            msg_req to_server = msg_req.newBuilder().setNomeJob(nomeJob).setTipoProcessing(tipoProcessing).setNomeFile(nomeFile).build();

            System.out.println("\n<-- ["+tipoProcessing+", "+nomeFile+", "+nomeJob+"]");

            this.stub.jobReq(to_server);

            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }

    public static void main(String[] args){

        int porto = Integer.parseInt(args[0]);
        ManagedChannel channel = Grpc.newChannelBuilder("localhost:"+porto, InsecureChannelCredentials.create()).build();

        JobsClient clientee = new JobsClient(channel);

        clientee.greet(Integer.parseInt(args[1]), args[2]);

        try {
            channel.shutdownNow().awaitTermination(5, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

}
