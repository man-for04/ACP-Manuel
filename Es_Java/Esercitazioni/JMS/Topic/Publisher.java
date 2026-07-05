package Esercitazioni.JMS.Topic;

import java.util.Hashtable;

import javax.jms.JMSException;
import javax.jms.Session;
import javax.jms.Topic;
import javax.jms.TopicConnection;
import javax.jms.TopicConnectionFactory;
import javax.jms.TopicPublisher;
import javax.jms.TopicSession;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.jms.TextMessage;

public class Publisher {
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
            
            TopicSession tSession = tConnection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
            
            TopicPublisher publisher= tSession.createPublisher(topic);

            TextMessage msg = tSession.createTextMessage();

            for(int i=0;i<3;i++){
                msg.setText("ciao "+i);
                publisher.send(msg);
                System.out.println("Messaggio "+msg.getText()+" pubblicato");
            }
            msg.setText("fine");
            publisher.send(msg);

            publisher.close();
            tConnection.close();
            tSession.close();


        } catch (NamingException | JMSException e) {
            e.printStackTrace();
        }
    }
}
