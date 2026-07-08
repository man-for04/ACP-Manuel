import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.Hashtable;

import javax.jms.*;
import javax.naming.*;


public class InfoFilter {
    public static void main (String[] args){

        Hashtable<String,String> jms_properties = new Hashtable<>();
        jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        jms_properties.put("queue.info", "info");

        try(PrintWriter out = new PrintWriter(new FileOutputStream("./info.txt"), true)) {
            
            InitialContext contesto = new InitialContext(jms_properties);
            QueueConnectionFactory qfactory = (QueueConnectionFactory)contesto.lookup("QueueConnectionFactory");
            //Li passerò al thread (sono safe)
            Queue queue_info = (Queue) contesto.lookup("info");
            QueueConnection qConnection = qfactory.createQueueConnection();

            QueueSession qSession = qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);

            QueueReceiver qReceiver = qSession.createReceiver(queue_info);


            qReceiver.setMessageListener(new InfoListener(out));
            qConnection.start();
            
            System.out.println("InfoFilter attivato!");
            
            try {
                Thread.sleep(60000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("InfoChecker chiuso");
            qReceiver.close();
            qSession.close();
            qConnection.close();

        } catch (NamingException |JMSException | FileNotFoundException e) {
            e.printStackTrace();
        }

    }
}
