import java.security.MessageDigest;

import javax.jms.*;

public class DispatcherMessageListener implements MessageListener{

    private QueueConnection qconnection;
    private int server_port;

    public DispatcherMessageListener(QueueConnection qconnection, 
                            int server_port
    );



    @Override
    public void onMessage(Message message) {
        //crea un nuovo thread dispatcher che gestirà la richiesta
        //e manderò una richoesya al server python (tramite il 
        // suo proxy), aspetterà la risposta dal server pythom
        //la risppsta la rimanderà al client python sulla coda response
        //la destination è ottenuta attraverso il campo JMSReplyTo

        //al thread cosa gli devo passare???
        //1. QueueConnection perchè? perchè devo creare una nuova sessione che mi permette di creare un QueueSender
        //2. passa il messaggio
        //3. il porto di comunicazione della socket TCP in listeing sul server python

        TextMessage text_message = (TextMessage) message;
        DispatcherThread dispatcher_thread = new DispatcherThread(server_port, 
                                                            qconnection, 
                                                            text_message);

        dispatcher_thread.start();
    }
}
