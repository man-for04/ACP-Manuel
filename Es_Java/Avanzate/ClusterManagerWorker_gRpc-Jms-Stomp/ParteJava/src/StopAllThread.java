import java.lang.Thread;
import javax.jms.*;

import PackageTask.*;

public class StopAllThread extends Thread{

    GestioneTaskImpl ref;
    Req_string req;

    Req_string request;
    public StopAllThread(Req_string request, GestioneTaskImpl ref){
        super();
        this.request = request;
        this.ref=ref;
    }

    @Override
    public void run() {
        String type = request.getType();

        try {
            TopicSession tSession = ref.tConnection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
            TopicPublisher pubGPU = tSession.createPublisher(ref.gpuTopic);
            TopicPublisher pubRT = tSession.createPublisher(ref.rtTopic);
            
            TextMessage msg = tSession.createTextMessage();
            msg.setText("stop_all");
            
            if(type.contains("gpu-bound")){
                pubGPU.publish(msg);

                System.out.println("-->Invocato stopAll gpu-bound, inviato: ["+msg.getText()+"]");
            }
            else if(type.contains("real-time")){
                pubRT.publish(msg);

                System.out.println("-->Invocato stopAll real-time, inviato:["+msg.getText()+"]");
            }
            else{
                System.out.println("ERRORE! Type della richiesta stop_all non valido! <"+ type+ ">");
            }

        } catch (JMSException e) {
            e.printStackTrace();
        }

        }
    }
    