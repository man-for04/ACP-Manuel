
import javax.jms.*;;

public class MioDispatcherListener implements MessageListener{

    int porto;
    QueueConnection qConnection;
    

    public MioDispatcherListener(int porto, QueueConnection qConnection){
        this.porto=porto;
        this.qConnection=qConnection;
    }


    @Override
    public void onMessage(Message message) {

        TextMessage msg = (TextMessage) message;
        try {
            String tipo_richiesta = msg.getText().split("#")[0];
            int id_articolo = Integer.parseInt(msg.getText().split("#")[1]);
            Queue queue = (Queue) msg.getJMSReplyTo();

            System.out.println("<Dispatcher> ho ricevuto messaggio jms contenente {tipo: "+tipo_richiesta+", id: "+ id_articolo +", coda: " +queue);

            DispatcherThread td = new DispatcherThread(porto, id_articolo, tipo_richiesta, qConnection, queue);
            td.start();
            //@Gemini: qui per il thread non andrebbe fatta la join? Nella risoluzione del prof lascia così "appeso"


        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
}
