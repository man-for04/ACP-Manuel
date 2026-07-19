import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.TextMessage;
import javax.jms.TopicPublisher;
import javax.jms.TopicSession;

public class ExtractorListener implements MessageListener{

    private TopicSession session;
    private TopicPublisher pub_temp;
    private TopicPublisher pub_press;

    public ExtractorListener(TopicSession session, TopicPublisher pub_temp, TopicPublisher pub_press){
        this.pub_press = pub_press;
        this.pub_temp = pub_temp;
        this.session = session;
    }

    @Override
    public void onMessage(Message message) {
        MapMessage from_client = (MapMessage) message;
        try {
            
            String type = from_client.getString("type");
            int value = from_client.getInt("value");

            System.out.println("--> ["+type+"-"+value+"]");

            TextMessage to_analyzer = session.createTextMessage(Integer.toString(value));

            if(type.equals("temperature")){
                
                pub_temp.publish(to_analyzer);
                System.out.println("<--Inviato su temp\n");

            }
            else if(type.equals("pressure")){
                
                pub_press.publish(to_analyzer);
                System.out.println("<--Inviato su press\n");
            }
            else{
                System.out.println("ERRORE! type non valido: "+type);
            }

        } catch (JMSException e) {
            e.printStackTrace();
        }
        
    }

}
