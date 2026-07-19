import mioPackage.TaskManagementGrpc.TaskManagementBlockingStub;
import mioPackage.TaskManagementOuterClass.msg_req_dep;
import mioPackage.TaskManagementOuterClass.msg_req_stop;

import java.util.Random;

public class ClientThread extends Thread{

    String[] types = {"gpu-bound", "cpu-bound"};

    final TaskManagementBlockingStub stub;

    public ClientThread(TaskManagementBlockingStub stub){
        this.stub = stub;
    }

    @Override
    public void run() {
        System.out.println("ClientThread attivato!");

        Random rand = new Random();
        
        for(int i=0;i<4;i++){
            //deploy
            int id = rand.nextInt(100, 1000);
            String name = "task"+Integer.toString(rand.nextInt(1,100));
            String type = types[rand.nextInt(0,2)];

            System.out.println("<-- Invio: "+id+", "+name+", "+ type);

            msg_req_dep to_manager = msg_req_dep.newBuilder().setId(id).setName(name).setType(type).build();

            stub.deploy(to_manager);

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        String type = types[rand.nextInt(0,2)];
        System.out.println("<-- Invio: "+ type);

        msg_req_stop to_manager = msg_req_stop.newBuilder().setType(type).build();

        stub.stopAll(to_manager);

    }
    
}
