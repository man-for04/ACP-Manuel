import java.lang.Thread;

import mioPackage.TaskManagementOuterClass.msg_req_stop;

public class StopAllThread2 extends Thread{

    private msg_req_stop req;

    public StopAllThread2(msg_req_stop y){
        this.req = y;
    }

    @Override
    public void run() {
        String type = req.getType();

        System.out.println("--> Ricevuto da client stop_all: "+ type);
        //TODO: Invia su topic
    }
    
}
