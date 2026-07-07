package PackageTask;

import java.util.Random;

public class ClientThread extends Thread{
    private final String[] task_types;
    private GestioneTaskGrpc.GestioneTaskBlockingStub proxy;

    public ClientThread(String[] task_types, GestioneTaskGrpc.GestioneTaskBlockingStub proxy){
        this.task_types = task_types;
        this.proxy = proxy;
    }

    @Override
    public void run() {

        Random rand = new Random();

        int id;
        String name;
        String type;

        for(int i=0;i<4;i++){

            id = rand.nextInt(999) +1 ;
            name = "task#" + Integer.toString(id);
            type = task_types[rand.nextInt(2)];

            proxy.deploy(Req_task.newBuilder().setId(id).setName(name).setType(type).build());
            System.out.println("Inviata richiesta deploy");

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        }
        type = task_types[rand.nextInt(2)];
        proxy.stopAll(Req_string.newBuilder().setType(type).build());
        System.out.println("Inviata richiesta stopAll");
    }

}
