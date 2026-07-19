import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;
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

public class CPUprocessor {

    public static void main(String[] args){

        //setup jms
            Hashtable<String, String> jms_properties = new Hashtable<>();
            /*"java.naming.factory.initial" -> "org.apache.activemq.jndi.ActiveMQInitialContextFactory"
            "java.naming.provider.url" -> "tcp://127.0.0.1:61616" */
            jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
            jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
            jms_properties.put("topic.cpu", "cpu");
    
            InitialContext contesto;
            try{
                contesto = new InitialContext(jms_properties);
                TopicConnectionFactory factory = (TopicConnectionFactory) contesto.lookup("TopicConnectionFactory");
                Topic topic_cpu = (Topic) contesto.lookup("cpu");
        
                TopicConnection connection = (TopicConnection) factory.createTopicConnection();
                TopicSession session = (TopicSession) connection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
    
                TopicSubscriber sub_cpu = session.createSubscriber(topic_cpu);
                PrintStream out = new PrintStream(new FileOutputStream("cpu.txt", true), true);
                sub_cpu.setMessageListener(new GPUprocessorListener(out));
                connection.start();
    
                System.out.println("Cpu Processor attivato!");

    
            } catch (NamingException | JMSException | FileNotFoundException e) {
                e.printStackTrace();
            }

    }

}
