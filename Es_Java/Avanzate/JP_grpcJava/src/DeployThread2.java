import java.lang.Thread;

import mioPackage.TaskManagementOuterClass.msg_req_dep;

public class DeployThread2 extends Thread{

    private msg_req_dep req;

    public DeployThread2(msg_req_dep y){
        this.req = y;
    }

    @Override
    public void run() {
        int id = req.getId();
        String name = req.getName();
        String type = req.getType();
        
        System.out.println("--> Ricevuto da client deploy: "+ id+", "+name+", "+type);
        //TODO: Invia su topic
    }
    
}
