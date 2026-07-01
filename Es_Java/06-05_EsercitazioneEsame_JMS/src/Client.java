import java.util.Hashtable;
import java.util.Random;

import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueReceiver;
import javax.jms.QueueSender;
import javax.jms.QueueSession;
import javax.jms.Session;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

//thread safe dalla singola produzione/consumazione, non da TUTTE

//vai a vedere gli esempi su github di durabile/non durabile

public class Client {
    public static void main(String[] args) throws NamingException, JMSException{ //in aula li ha gestiti con try-catch
        String corrID = args[0];
		
		Hashtable <String, String> p = new Hashtable <String, String>();
		
		p.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
		p.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
		
		p.put("queue.Richiesta", "Richiesta");
		p.put("queue.Risposta", "Risposta");
		
		Context ctx = new InitialContext ( p );
		
		QueueConnectionFactory qconnf = (QueueConnectionFactory)ctx.lookup("QueueConnectionFactory");
		
		Queue queueRequest = (Queue) ctx.lookup("Richiesta");
		Queue queueResponse = (Queue) ctx.lookup("Risposta");
		
		QueueConnection qconn = qconnf.createQueueConnection();
		qconn.start();
		
		QueueSession qsession = qconn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);

		// Setup del receiver per la coda di messaggi Risposta
		// Setto il message selector in maniera tale che il receiver riceva solo i messaggi che contengono il suo correlation ID
		QueueReceiver qr = qsession.createReceiver(queueResponse, "JMSCorrelationID='" + corrID + "'"); //ho 2 metodi: 1 classico (ricevi su tutto), l'altro che mi fa specificare il CorrelationID ⭕Attenzione, va fatto per evitare di "prendermi tutto" più avanti TODO
		ClientListener listener = new ClientListener();
		qr.setMessageListener(listener); //dà errore perchè la classe non implementa MessageListener
		
		// Setup del sender per la coda di messaggi Richiesta
		QueueSender sender = qsession.createSender(queueRequest);
		MapMessage message = qsession.createMapMessage(); //⭕su mapMessage posso usare tutti i metodi per settare chiave e valore

        for(int i=0; i<10; i++){
            if(i%2 == 0){ //genera messaggi di deposito

                /*
                ('operazione', 'deposita') e
                ('valore', id_articolo)
                */
                message.setString("operazione", "deposita");
                message.setInt("valore", 1); //Andare a decodificare usando questi metodi, il campo indicato è la chiave
                message.setJMSCorrelationID(corrID); //uso tale header per specificare correlation  -> così quando vado a inizializzare Receiver prendo solo quello che ho specificato
                message.setJMSReplyTo(queueResponse);//permette di specificare direttamente su quale coda mi aspetto le risposte (parametro è proprio una destination) --> qunado riceverò tale messaggio lato magazzino, otterrà un oggetto che viene già gestito da JMS (non servirà lookup di risposta) ⭕vedi la tabella slide 56, la conversione compare lì TODO

                sender.send(message);
                System.out.println("messaggio mandato...");
            }
            else{ //genera messaggi di prelievo
                
            }
        }
    }
}
