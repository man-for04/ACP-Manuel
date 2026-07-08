import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.Hashtable;

import javax.jms.*;
import javax.naming.*;


public class ErrorChecker {
    public static void main (String[] args){

        String stringa_input = args[0];

        Hashtable<String,String> jms_properties = new Hashtable<>();
        jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        jms_properties.put("queue.error", "error");

        try(PrintWriter out = new PrintWriter(new FileOutputStream("./error.txt"),true)){

            InitialContext contesto = new InitialContext(jms_properties);
            QueueConnectionFactory qfactory = (QueueConnectionFactory)contesto.lookup("QueueConnectionFactory");
            //Li passerò al thread (sono safe)
            Queue queue_error = (Queue) contesto.lookup("error");
            QueueConnection qConnection = qfactory.createQueueConnection();

            QueueSession qSession = qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);

            QueueReceiver qReceiver = qSession.createReceiver(queue_error);

            System.out.println("ErrorChecker attivato!");


            qReceiver.setMessageListener(new ErrorListener(stringa_input, out));

            qConnection.start();
            
            try {
                Thread.sleep(60000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("ErrorChecker chiuso");
            qReceiver.close();
            qSession.close();
            qConnection.close();

        } catch (NamingException |JMSException | FileNotFoundException e) {
            e.printStackTrace();
        }

    }
}
