import java.util.Hashtable;
import java.util.Scanner;

import javax.jms.*;
import javax.naming.*;

public class Dispatcher {
    //deve usare DispatcherProxy

    public static void main(String[] args){
        //Setup
        System.out.println("Ciao, sono il dispatcher!");

        System.out.print("Inserire porto del server: ");
        Scanner s = new Scanner(System.in);
        int porto = s.nextInt();
        s.close();

        
        //LATO JMS: PRELEVA RICHIESTE
        Hashtable<String, String> jms_properties = new Hashtable<>();
        jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        /*"java.naming.factory.initial" -> "org.apache.activemq.jndi.ActiveMQInitialContextFactory"
        "java.naming.provider.url" -> "tcp://127.0.0.1:61616" */
        jms_properties.put("queue.Richiesta", "Richiesta");

        InitialContext context;
        try {
            context = new InitialContext(jms_properties);
            QueueConnectionFactory qfactory = (QueueConnectionFactory) context.lookup("QueueConnectionFactory");
            Queue queue = (Queue) context.lookup("Richiesta");

            QueueConnection qConnection = qfactory.createQueueConnection();

            
            QueueSession qSession = qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            //qSession.setMessageListener(new MioDispatcherListener(porto, qConnection));
            
            QueueReceiver qReceiver = qSession.createReceiver(queue);
            qReceiver.setMessageListener(new MioDispatcherListener(porto, qConnection));

            qConnection.start();

            System.out.println("<DISPATCHER> Connessione al Client instaurata!");

            try {
                Thread.sleep(60000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            };

            qConnection.close();
            qSession.close();


        } catch (NamingException  | JMSException e) {
            e.printStackTrace();
        }

    }
}
