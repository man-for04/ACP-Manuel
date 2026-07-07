import PackageTask.Req_task;
import javax.jms.*;

public class DepolyThread extends Thread{

    GestioneTaskImpl ref;
    Req_task req;


    Req_task request;
    public DepolyThread(Req_task request, GestioneTaskImpl ref){
        super();
        this.request = request;
        this.ref=ref;
    }

    @Override
    public void run() {
        int id = request.getId();
        String name = request.getName();
        String type = request.getType();

        //Setup jms
        try {
            TopicSession tSession = ref.tConnection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
            TopicPublisher pubGPU = tSession.createPublisher(ref.gpuTopic);
            TopicPublisher pubRT = tSession.createPublisher(ref.rtTopic);
            
            
            if(type.contains("gpu-bound")){
                TextMessage msg = tSession.createTextMessage();
                msg.setText("deploy-"+id+"-"+name);
                pubGPU.publish(msg);
                
                System.out.println("--->Invocato deploy gpu-bound: invio [" + msg.getText()+"]");
            }
            else if(type.contains("real-time")){
                TextMessage msg = tSession.createTextMessage();
                msg.setText("deploy-"+id+"-"+name);
                pubRT.publish(msg);

                System.out.println("--->Invocato deploy real-time: invio [" + msg.getText()+"]");
        }
        else{
            System.out.println("ERRORE! Type della richiesta non valido! <"+ type+ ">");
        }

    } catch (JMSException e) {
        e.printStackTrace();
    }

    }
    
}
