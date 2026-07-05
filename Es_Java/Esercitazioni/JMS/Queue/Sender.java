package Esercitazioni.JMS.Queue;

import java.util.Hashtable;

import javax.jms.*;
import javax.naming.*;


public class Sender {
    public static void main(String[] args){

        Hashtable<String, String> jms_properties = new Hashtable<>();

        jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        jms_properties.put("queue.miacoda", "miacoda");

        //lookup
        try {
            InitialContext contesto = new InitialContext(jms_properties);
            QueueConnectionFactory qFactory = (QueueConnectionFactory) contesto.lookup("QueueConnectionFactory");
            Queue queue = (Queue) contesto.lookup("miacoda");

            QueueConnection qconnection = qFactory.createQueueConnection();

            QueueSession qsession = qconnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);

            QueueSender sender = qsession.createSender(queue);

            System.out.println("Ciao, sono il sender");
            TextMessage msg;

            for(int i=0;i<3;i++){
                msg = qsession.createTextMessage();
                msg.setText("Ciao n. "+i);
                System.out.println("Invio messaggio... " +msg.getText());

                sender.send(msg);
            }
            msg = qsession.createTextMessage();
            msg.setText("fine");
            sender.send(msg);


            sender.close();
            qsession.close();
            qconnection.close();


        } catch (NamingException | JMSException e) {
            e.printStackTrace();
        }
    }
}
