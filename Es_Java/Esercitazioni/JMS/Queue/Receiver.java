package Esercitazioni.JMS.Queue;

import java.util.Hashtable;

import javax.jms.JMSException;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueReceiver;
import javax.jms.QueueSession;
import javax.jms.Session;
import javax.jms.TextMessage;
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class Receiver {
    //Setup di hashtable
    public static void main (String[] args){
        Hashtable<String, String>  jms_properties = new Hashtable<>();
        jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        jms_properties.put("queue.miacoda", "miacoda");


        //passo al lookup
        try {
            InitialContext contesto = new InitialContext(jms_properties);

            QueueConnectionFactory qFactory = (QueueConnectionFactory) contesto.lookup("QueueConnectionFactory");
            Queue queue = (Queue) contesto.lookup("miacoda");

            QueueConnection qconnection = (QueueConnection) qFactory.createQueueConnection();
            qconnection.start();

            QueueSession qSession = qconnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);

            QueueReceiver receiver= qSession.createReceiver(queue);

            System.out.println("Ciao, sono il receiver");

            TextMessage msg;

            do{
                msg = (TextMessage) receiver.receive();
                System.out.println("Ho ricevuto messaggio: "+msg.getText());

            }while(!msg.getText().equals("fine"));

            receiver.close();
            qSession.close();
            qconnection.close();

        } catch (NamingException | JMSException e) {
            e.printStackTrace();
        }
    }
}
