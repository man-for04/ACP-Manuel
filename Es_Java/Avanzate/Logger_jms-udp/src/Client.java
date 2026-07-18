package src;
import java.util.Hashtable;

import javax.jms.*;
import javax.naming.InitialContext;
import javax.naming.NamingException;


public class Client {
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

            TopicPublisher pub = session.createPublisher(topic);

            int dato = Integer.parseInt(args[0]);
            int porta = Integer.parseInt(args[1]);

            System.out.println("<-- Invio: "+dato+", "+porta);

            MapMessage to_disk = session.createMapMessage();
            to_disk.setInt("dato", dato);
            to_disk.setInt("porta", porta);

            pub.publish(to_disk);
            //System.out.println("Inviato: "+to_disk);

            pub.close();
            session.close();
            connection.close();


        } catch (NamingException e) {
            e.printStackTrace();
        } catch (JMSException e) {
            e.printStackTrace();
        }

        
    }
}
