import java.io.FileNotFoundException;
import java.util.Hashtable;

import javax.jms.*;
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class WorkerCPU {

    public static void main(String[] args){
        Hashtable<String, String> jms_properties = new Hashtable<>();
        jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        jms_properties.put("topic.CPU", "CPU");

        /*"java.naming.factory.initial" -> "org.apache.activemq.jndi.ActiveMQInitialContextFactory"
        "java.naming.provider.url" -> "tcp://127.0.0.1:61616" */

        try {
            InitialContext contesto = new InitialContext(jms_properties);
            TopicConnectionFactory tfactory = (TopicConnectionFactory) contesto.lookup("TopicConnectionFactory");
            Topic cpu_topic = (Topic) contesto.lookup("CPU");

            TopicConnection tconnection = (TopicConnection) tfactory.createTopicConnection();

            TopicSession tsession = (TopicSession) tconnection.createSession(false, Session.AUTO_ACKNOWLEDGE);

            TopicSubscriber sub = tsession.createSubscriber(cpu_topic);

            sub.setMessageListener(new ListenerCPU());

            tconnection.start();
            System.out.println("Connessione cpu avviata! ");


        } catch (NamingException | JMSException | FileNotFoundException e) {
            e.printStackTrace();
        };

    }

    


}
