import java.util.Hashtable;
import java.util.Random;

import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Session;
import javax.jms.Topic;
import javax.jms.TopicConnection;
import javax.jms.TopicConnectionFactory;
import javax.jms.TopicPublisher;
import javax.jms.TopicSession;
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class Client {
    public static void main(String[] args){

        String[] values_buy = {"Jovanotti", "Ligabue", "Negramaro"};

        Hashtable<String, String> jms_properties = new Hashtable<>();
        jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        /* "java.naming.factory.initial" -> "org.apache.activemq.jndi.ActiveMQInitialContextFactory"
        "java.naming.provider.url" -> "tcp://127.0.0.1:61616"*/

        jms_properties.put("topic.request", "request");

        try {
            InitialContext contesto = new InitialContext(jms_properties);
            TopicConnectionFactory tfactory = (TopicConnectionFactory) contesto.lookup("TopicConnectionFactory");
            Topic request_topic = (Topic) contesto.lookup("request");

            TopicConnection tConnection = tfactory.createTopicConnection();
            TopicSession tSession = tConnection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);

            TopicPublisher pub_request = tSession.createPublisher(request_topic);

            System.out.println("Client connesso!\n\n");
            
            String type = args[0];
            String value;
            Random rand = new Random();

            if(type.equals("buy")){
                //Caso buy
                for(int i=0;i<20;i++){
                    //Genero la i-esima richiesta
                    
                    value = values_buy[rand.nextInt(3)];

                    MapMessage to_manager = tSession.createMapMessage();
                    to_manager.setString("type", type);
                    to_manager.setString("value", value);

                    pub_request.publish(to_manager);
                    System.out.println("<--Inviato {"+type+", "+value+"}\n");
                    
                    try {
                        Thread.sleep(2000); //Attente 2 secondo tra le richieste
                    }
                    catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                }
            }
            else if(type.equals("stats")){
                value = "Sold";
                //caso stats
                for(int i=0;i<20;i++){
                    //Genero la i-esima richiesta
                    MapMessage to_manager = tSession.createMapMessage();
                    to_manager.setString("type", type);
                    to_manager.setString("value", value);

                    pub_request.publish(to_manager);
                    System.out.println("<--Inviato {"+type+", "+value+"}\n");
                    
                    try {
                        Thread.sleep(2000); //Attente 2 secondo tra le richieste
                    }
                    catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                }
            }
            else{
                System.out.println("ERRORE! type inserito: "+type+" non riconosciuto");
            }

            pub_request.close();
            tSession.close();
            tConnection.close();

            System.out.println("\n\nFINITO!");

        } catch (NamingException | JMSException e) {
            e.printStackTrace();
        }

        
        
    }
}
