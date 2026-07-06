import javax.jms.*;

public class DispatcherThread extends Thread{
    private int porto;
    private int id_articolo;
    private String tipo_richiesta;
    private QueueConnection qConnection;
    private Queue queue;
    
    public DispatcherThread(int porto, int id_articolo, String tipo_richiesta, QueueConnection qConnection, Queue queue){
        super();
        this.porto=porto;
        this.id_articolo=id_articolo;
        this.tipo_richiesta=tipo_richiesta;
        this.qConnection=qConnection;
        this.queue = queue;
    }

    @Override
    public void run(){
        System.out.println("Ciao, sono nuovo thread dispatcher");

        try {
            sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        DispatcherProxy proxy = new DispatcherProxy(porto);

        if(tipo_richiesta.equals("deposita")){
            System.out.println("<DispatcherThread> Ricevuta richiesta di depositare");
            proxy.deposita(id_articolo);

            System.out.println("<DispatcherThread> Inviata richiesta di deposito "+id_articolo);

            try {
                QueueSession qsession = qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
                QueueSender sender = qsession.createSender(queue);

                TextMessage risposta = qsession.createTextMessage();
                risposta.setText("deposited");
                sender.send(risposta);
                System.out.println("<Dispatcher> ho inviato RISPOSTA: "+risposta.getText());

                sender.close();
                qsession.close();

            } catch (JMSException e) {
                e.printStackTrace();
            }

        }
        else if(tipo_richiesta.equals("preleva")){
            System.out.println("<DispatcherThread> Ricevuta richiesta di prelevare");
            int elem = proxy.preleva();
            
            System.out.println("<DispatcherThread> Prelevato valore "+elem);

            try {
                QueueSession qsession = qConnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
                QueueSender sender = qsession.createSender(queue);

                TextMessage risposta = qsession.createTextMessage();
                risposta.setText(Integer.toString(elem));
                sender.send(risposta);
                System.out.println("<Dispatcher> ho inviato RISPOSTA: "+risposta.getText());

                sender.close();
                qsession.close();

            } catch (JMSException e) {
                e.printStackTrace();
            }

        }
        else{
            System.out.println("ERRORE dispatcher! Richiesta non valida!");
        }

    }
}
