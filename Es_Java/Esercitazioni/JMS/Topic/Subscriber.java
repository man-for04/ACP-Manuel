package Esercitazioni.JMS.Topic;

import java.util.Hashtable;

import javax.jms.JMSException;
import javax.jms.Session;
import javax.jms.Topic;
import javax.jms.TopicConnection;
import javax.jms.TopicConnectionFactory;
import javax.jms.TopicSession;
import javax.jms.TopicSubscriber;
import javax.naming.InitialContext;
import javax.naming.NamingException;

//Voglio fare caso ASINCRONO (con listener)
public class Subscriber {

    public static void main(String[] args){

        Hashtable<String, String> jms_properties = new Hashtable<>();

        jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        
        jms_properties.put("topic.miotopic", "miotopic");
        

        try {
            InitialContext context = new InitialContext(jms_properties);

            TopicConnectionFactory tfactory = (TopicConnectionFactory) context.lookup("TopicConnectionFactory");
            Topic topic = (Topic) context.lookup("miotopic");

            TopicConnection tConnection = tfactory.createTopicConnection();
            tConnection.setClientID("cliente1");

            
            TopicSession tSession = tConnection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
            
            TopicSubscriber subscriber= tSession.createDurableSubscriber(topic, "sub1");
            
            
            subscriber.setMessageListener(new MioListener());
            
            tConnection.start();

            System.out.println("In attesa di leggere...");

            try {
                Thread.sleep(20000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            };

            subscriber.close();
            tConnection.close();
            tSession.close();
            


        } catch (NamingException | JMSException e) {
            e.printStackTrace();
        }
    }
}
