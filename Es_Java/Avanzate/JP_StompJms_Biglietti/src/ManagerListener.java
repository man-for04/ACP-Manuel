

import java.io.PrintWriter;

import javax.jms.*;

public class ManagerListener implements MessageListener{

    TopicSession tSession;
    TopicPublisher tickets_publisher;
    TopicPublisher stats_publisher;
    PrintWriter out;

    public ManagerListener(TopicSession tSession, TopicPublisher tickets_publisher, TopicPublisher stats_publisher, PrintWriter out) {
        this.tSession = tSession;
        this.tickets_publisher = tickets_publisher;
        this.stats_publisher = stats_publisher;
        this.out = out;
    }

    @Override
    public void onMessage(Message message) {
        //ricezione asincrona su topic request
        MapMessage request = (MapMessage) message;
        
        try {


            //gestione jms uscita
            
            

            
            //unpacking
            String type = request.getString("type");
            String value = request.getString("value");

            System.out.println("--> Listener ha ottenuto: {"+type+", "+value+"}");

            //valutazione
            if(type.equals("stats")){ //@Gemini: che accade con contains?
                //caso stats

                TextMessage to_stats = tSession.createTextMessage(value);
                
                
                stats_publisher.publish(to_stats);

                System.out.println("<-- Invio su stats {"+value+"}\n");

            }
            else if (type.equals("buy")){
                //caso buy

                out.println(value);
                TextMessage to_stats = tSession.createTextMessage(value);
                tickets_publisher.publish(to_stats);

                System.out.println("<-- Invio su tickets {"+value+"} e scritto su file\n");
            }
            else{
                System.out.println("\n\nERRORE! type non riconosciuto: "+type+"\n\n");
            }
            
        } catch (JMSException e) {
            e.printStackTrace();
        }
        
    }
    

}
