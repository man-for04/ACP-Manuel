package src;
import java.util.Hashtable;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.jms.*;
import java.lang.Thread;

public class Disk {
    
    public static void main(String[] args){
        //setup JMS
            Hashtable<String, String> jms_properties = new Hashtable<>();
            /*"java.naming.factory.initial" -> "org.apache.activemq.jndi.ActiveMQInitialContextFactory"
            "java.naming.provider.url" -> "tcp://127.0.0.1:61616"
             */
            jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
            jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
            jms_properties.put("topic.storage", "storage");
    
            InitialContext contesto;
            try {
                contesto = new InitialContext(jms_properties);
                TopicConnectionFactory factory = (TopicConnectionFactory) contesto.lookup("TopicConnectionFactory");
                Topic topic = (Topic) contesto.lookup("storage");
    
                TopicConnection connection = (TopicConnection) factory.createTopicConnection();
                TopicSession session = (TopicSession) connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
    
                TopicSubscriber sub = session.createSubscriber(topic);
    
                sub.setMessageListener(new DiskListener());
    
                connection.start();
    
                System.out.println("Disk in ascolto...");
    
                Thread.sleep(60000);
    
                sub.close();
                session.close();
                connection.close();
    
    
            } catch (NamingException e) {
                e.printStackTrace();
            } catch (JMSException e2) {
                e2.printStackTrace();
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }

    }
    
}
