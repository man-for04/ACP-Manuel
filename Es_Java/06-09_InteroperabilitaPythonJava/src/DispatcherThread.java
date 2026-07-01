import javax.jms.*;

public class DispatcherThread extends Thread{

    private int server_port;
    private QueueConnection qconnection;
    private TextMessage message;

    public DispatcherThread(int server_port, 
                    QueueConnection qConnection, ){

    }

    public void run(){
        //1. istanziare il mio proxy per fare proxy.deposita o proxy.preleva
        
        JService proxy = new DispatcherProxy("localhost", server_port);

        try{
            String richiesta  = message.getText();
            Queue queue_response = (Queue) message.getJMSReplyTo();

            if(richiesta.equalsIgnoreCase("preleva")){

                int valore_prelevato = proxy.preleva();
                String result_to_send = new String(Integer.valueOf(valore_prelevato));

            }else if (richiesta.contains("deposita")){

                //splitta sulla stringa richiesta per prendere il valore da depositare

                String messaggio_splitted = richiesta.split("-");
                int valore_da_depositare = Integer.valueOf(messaggio_splitted[1]);

                proxy.desposita(valore_da_depositare);
                
                String result_to_send = new String("deposited");

            }
            Queue queue_response = (Queue) message.getJMSReplyTo();

            //invia results_to_send sulla coda queue_response

            QueueSession qsession = qconnection.createQueueSession(false,);
            QueueSender qsender = qsession.createSender(queue_response);
            TextMessage text_message = session.createTextMessage(result_to_send);

            qsender.send(text_message);

            qsender.close();
            session.close()
        }
        catch(JMSException e){

        }

        proxy.deposita();
        proxy.preleva();

        //2. devo rispondere al client sulla coda response da prendere nel campo JMSReplyTo del messaggio di richiesta
    }
}
