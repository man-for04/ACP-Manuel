import java.util.Hashtable;

import javax.jms.JMSException;
import javax.jms.TopicConnection;
import javax.jms.TopicConnectionFactory;
import javax.jms.TopicPublisher;
import javax.jms.TopicSession;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.jms.*;

public class Extractor {


    public static void main(String[] args){

         //setup jms
        Hashtable<String, String> jms_properties = new Hashtable<>();
        /*"java.naming.factory.initial" -> "org.apache.activemq.jndi.ActiveMQInitialContextFactory"
        "java.naming.provider.url" -> "tcp://127.0.0.1:61616" */
        jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        jms_properties.put("topic.data", "data");
        jms_properties.put("topic.temp", "temp");
        jms_properties.put("topic.press", "press");
        

        try {
            InitialContext contesto = new InitialContext(jms_properties);

            TopicConnectionFactory factory = (TopicConnectionFactory) contesto.lookup("TopicConnectionFactory");
            Topic topic_data = (Topic) contesto.lookup("data");
            Topic topic_temp = (Topic) contesto.lookup("temp");
            Topic topic_press = (Topic) contesto.lookup("press");

            TopicConnection connection = factory.createTopicConnection();

            TopicSession session = connection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);

            TopicSubscriber sub_data = (TopicSubscriber) session.createSubscriber(topic_data);
            TopicPublisher pub_temp = (TopicPublisher) session.createPublisher(topic_temp);
            TopicPublisher pub_press = (TopicPublisher) session.createPublisher(topic_press);

            
            sub_data.setMessageListener(new ExtractorListener(session, pub_temp, pub_press));

            connection.start();
            System.out.println("Extractor in ascolto...");

            while(true){
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
    }
    catch (NamingException | JMSException e) {
            e.printStackTrace();
        }
    }
}
