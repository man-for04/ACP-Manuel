package Esercitazioni.JMS.Topic;
import javax.jms.*;

public class MioListener implements MessageListener{

    @Override
    public void onMessage(Message message) {
        TextMessage mess = (TextMessage) message;
        try {
            System.out.println("<MessageListener> ho ricevuto messaggio "+mess.getText());

        } catch (JMSException e) {
            e.printStackTrace();
        }
    }
    
}
