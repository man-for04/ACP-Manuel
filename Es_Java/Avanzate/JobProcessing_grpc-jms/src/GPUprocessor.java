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

public class GPUprocessor {

    public static void main(String[] args){

        //setup jms
            Hashtable<String, String> jms_properties = new Hashtable<>();
            /*"java.naming.factory.initial" -> "org.apache.activemq.jndi.ActiveMQInitialContextFactory"
            "java.naming.provider.url" -> "tcp://127.0.0.1:61616" */
            jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
            jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
            jms_properties.put("topic.gpu", "gpu");
    
            InitialContext contesto;
            try{
                contesto = new InitialContext(jms_properties);
                TopicConnectionFactory factory = (TopicConnectionFactory) contesto.lookup("TopicConnectionFactory");
                Topic topic_gpu = (Topic) contesto.lookup("gpu");
        
                TopicConnection connection = (TopicConnection) factory.createTopicConnection();
                TopicSession session = (TopicSession) connection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
    
                TopicSubscriber sub_gpu = session.createSubscriber(topic_gpu);
                PrintStream out = new PrintStream(new FileOutputStream("gpu.txt", true), true);
                sub_gpu.setMessageListener(new GPUprocessorListener(out));
                connection.start();
    
                System.out.println("Gpu Processor attivato!");

    
            } catch (NamingException | JMSException | FileNotFoundException e) {
                e.printStackTrace();
            }

    }

}
