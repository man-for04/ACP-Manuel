//Implementa 'la logica', senza riferimenti alle socket

import java.util.Hashtable;

import javax.jms.*;
import javax.naming.*;

import javax.jms.QueueConnection;
import javax.jms.QueueConnectionFactory;

public class LoggingImpl extends SkeletonLogging{

    QueueConnection qConnection;
    Queue queue_error;
    Queue queue_info;

    public LoggingImpl(int port) {

        super(port);

        Hashtable<String,String> jms_properties = new Hashtable<>();
        jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        jms_properties.put("queue.error", "error");
        jms_properties.put("queue.info", "info");

        /*"java.naming.factory.initial" -> "org.apache.activemq.jndi.ActiveMQInitialContextFactory"
        "java.naming.provider.url" -> "tcp://127.0.0.1:61616" */

        InitialContext contesto;
        try {
            contesto = new InitialContext(jms_properties);
            QueueConnectionFactory qfactory = (QueueConnectionFactory)contesto.lookup("QueueConnectionFactory");
            //Li passerò al thread (sono safe)
            queue_error = (Queue) contesto.lookup("error");
            queue_info = (Queue) contesto.lookup("info");
            qConnection = qfactory.createQueueConnection();

        } catch (NamingException |JMSException e) {
            e.printStackTrace();
        }

    }


    @Override
    public synchronized void log(String messaggioLog, int tipo) {

        System.out.println("<ServerLogging> invocato metodo log");

        LoggingThread td = new LoggingThread(messaggioLog, tipo, qConnection, queue_error, queue_info);

        System.out.println("<ServerLogging> avvio thread...");
        td.start();
    }

}
