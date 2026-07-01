
import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Message;
import javax.jms.MessageListener;
public class ClientListener implements MessageListener{

    @Override
    public void onMessage(Message message) {
        // TODO Auto-generated method stub
        MapMessage msg = (MapMessage)message;
        try{
            System.out.println("messaggio ricevuto... valore: "+msg.getInt("valore"));
            System.out.println("JMSCorrelationID" + msg.getJMSCorrelationID());
        }
        catch(JMSException e){
            //TODO
            e.printStackTrace();
        }

    }
}

//🔗tutto il codice è nel progetto: https://github.com/ACP-unina/acp_materiale/blob/main/Esercitazioni/02_JAVA/03_EsercitazioneJMS/Esercitazione-JMS-1/src/magazzino/Magazzino.java


