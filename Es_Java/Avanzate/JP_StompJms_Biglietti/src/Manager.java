import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.Hashtable;

import javax.jms.*;
import javax.naming.*;

public class Manager {

    public static void main(String[] args){

        Hashtable<String, String> jms_properties = new Hashtable<>();
        jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        /* "java.naming.factory.initial" -> "org.apache.activemq.jndi.ActiveMQInitialContextFactory"
        "java.naming.provider.url" -> "tcp://127.0.0.1:61616"*/

        jms_properties.put("topic.request", "request");
        jms_properties.put("topic.tickets", "tickets");
        jms_properties.put("topic.stats", "stats");

        InitialContext contesto;
        try(PrintWriter out = new PrintWriter(new FileOutputStream("tickets.txt"), true)) {

            contesto = new InitialContext(jms_properties);
            TopicConnectionFactory tfactory = (TopicConnectionFactory) contesto.lookup("TopicConnectionFactory");
            Topic request_topic = (Topic) contesto.lookup("request");
            Topic tickets_topic = (Topic) contesto.lookup("tickets");
            Topic stats_topic = (Topic) contesto.lookup("stats");
    
            TopicConnection tConnection = tfactory.createTopicConnection();
            TopicSession tSession = tConnection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);



            //Ascolto di request
            TopicSubscriber request_subscriber = tSession.createSubscriber(request_topic);
            request_subscriber.setMessageListener(new ManagerListener(tConnection, tickets_topic, stats_topic, out));

            tConnection.start();
    
            System.out.println("Server connesso!\n\n");


            try {
                while(true){
                    Thread.sleep(1000);
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            request_subscriber.close();
            tConnection.close();
            tSession.close();
            
        } catch (NamingException |JMSException | FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

}
