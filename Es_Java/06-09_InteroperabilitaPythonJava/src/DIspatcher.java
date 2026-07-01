import java.util.Hashtable;

import javax.jms.JMSException;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueReceiver;
import javax.jms.QueueSession;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

import org.springframework.jms.JmsException;

public class DIspatcher {
    //Devo creare un peer per andare a comunicare con un server su un dato porto

    public static void main(String[] args){

        int python_server_port = Integer.valueOf(args[0]);
        //⭕ Qui vai in readME_pdf -> copia le prime 2 righe di Java JMS
        Hashtable<String, String> prop = new Hashtable<>();

        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");

        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        

        prop.put("queue.request", "request");
        prop.put("queue.response", "response");

        try{
            Context jndi_context = new InitialContext(prop); //ce ne sono vari che posso usare, ma mi basta questo
            QueueConnectionFactory queue_conn_factory = (QueueConnectionFactory) jndi_context.lookup("QueueConnectionFactory"); //Stesso nome della classe che sto creando 
            Queue queue_request = (Queue) jndi_context.lookup("request");

            QueueConnection queue_connection = queue_conn_factory.createQueueConnection();


            queue_connection.start(); //questo perchè devo ricevere qualcosa

            QueueSession qsession = queue_connection.createQueueSession(false, );

            QueueReceiver receiver = qsession.createReceiver(queue_request);

        }
        catch(NamingException e){
            //TODO: da gestire
            e.printStackTrace();
        }
        catch (JMSException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }
}
