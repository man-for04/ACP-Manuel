import java.lang.Thread;
import java.util.Hashtable;

import javax.jms.*;
import javax.naming.*;

public class LoggingThread extends Thread{
    private String messaggioLog;
    private int tipo;
    QueueConnection qConnection;
    Queue queue_error;
    Queue queue_info;

    public LoggingThread(String messaggioLog, int tipo, QueueConnection qConnection, Queue queue_error, Queue queue_info){
        super();
        this.messaggioLog=messaggioLog;
        this.tipo=tipo;
        this.qConnection=qConnection;
        this.queue_error=queue_error;
        this.queue_info=queue_info;
    }

    @Override
    public void run() {
        //Comportamento
        //Client jms queue
        try {
            //Creo le mie essendo non thread-safe
            
            QueueSession qSession = qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);

            QueueSender sender_error = qSession.createSender(queue_error);
            QueueSender sender_info = qSession.createSender(queue_info);

            //Vera logica
            MapMessage message = qSession.createMapMessage();
            message.setString("messaggioLog", messaggioLog);
            message.setInt("tipo", tipo);

            if(tipo == 2){
                System.out.println("<LoggingThread> invio {"+messaggioLog+"/"+tipo+"} su ERRORqueue");
                sender_error.send(message);
            }
            else if (tipo==1 || tipo == 0){
                System.out.println("<LoggingThread> invio {"+messaggioLog+"/"+tipo+"} su INFOqueue");
                sender_info.send(message);
            }
            else{
                System.out.println("<LoggingThread> ERRORE {"+messaggioLog+"/"+tipo+"} non riconosciuto");
            }



        } catch (JMSException e) {
            e.printStackTrace();
        }
        
    }

    

}
