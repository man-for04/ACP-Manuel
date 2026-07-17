import java.util.Hashtable;

import javax.naming.InitialContext;
import javax.naming.NamingException;

import javax.jms.*;

public class ThreadConsumatore extends Thread{
    MiaCoda queue;

    String data;

    public ThreadConsumatore(MiaCoda quue){
        this.queue=quue;
    }

    @Override
    public void run(){
        System.out.println("Thread consumatore avviato");

        try {
            
            
            //STOMP - 1 solo thread, posso creare anche tutto qui
            /*"java.naming.factory.initial" -> "org.apache.activemq.jndi.ActiveMQInitialContextFactory"
            "java.naming.provider.url" -> "tcp://127.0.0.1:61616" */
            
            Hashtable<String, String> jms_properties = new Hashtable<>();
            jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
            jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
            jms_properties.put("queue.low", "low");
            jms_properties.put("queue.mid", "mid");
            jms_properties.put("queue.high", "high");

            InitialContext contesto = new InitialContext(jms_properties);
            QueueConnectionFactory qfactory = (QueueConnectionFactory) contesto.lookup("QueueConnectionFactory");
            Queue qlow = (Queue) contesto.lookup("low");
            Queue qmid = (Queue) contesto.lookup("mid");
            Queue qhigh = (Queue) contesto.lookup("high");
            
            QueueConnection qConnection = qfactory.createQueueConnection();
            QueueSession qSession = qConnection.createQueueSession(false,Session.AUTO_ACKNOWLEDGE );
            
            QueueSender sender_low = qSession.createSender(qlow);
            QueueSender sender_mid = qSession.createSender(qmid);
            QueueSender sender_high = qSession.createSender(qhigh);

            
            while(true){
                
                    data = queue.preleva();
                    System.out.println("== Prelevato da coda "+data);
    
                    TextMessage to_checker = qSession.createTextMessage(data);

                    if(data.contains("LOW")){
                        sender_low.send(to_checker);
                    }
                    else if(data.contains("MID")){
                        sender_mid.send(to_checker);

                    }
                    else if(data.contains("HIGH")){
                        sender_high.send(to_checker);
                    }
                    else{
                        System.out.println("ERRORE tipo non riconosciuto");
                    }
                    System.out.println("<-- Inviato su una delle 3 code "+data + "\n\n");
                }
    
        }catch (NamingException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (JMSException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
