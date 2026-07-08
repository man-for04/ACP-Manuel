

import java.io.PrintWriter;

import javax.jms.*;

public class ManagerListener implements MessageListener{

    TopicConnection tConnection;
    Topic tickets_topic;
    Topic stats_topic;
    PrintWriter out;

    public ManagerListener(TopicConnection tConnection, Topic tickets_topic, Topic stats_topic, PrintWriter out) {
        this.tConnection = tConnection;
        this.tickets_topic = tickets_topic;
        this.stats_topic = stats_topic;
        this.out = out;
    }

    @Override
    public void onMessage(Message message) {
        //ricezione asincrona su topic request
        MapMessage request = (MapMessage) message;
        
        try {


            //gestione jms uscita
            TopicSession tSession = tConnection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
            TopicPublisher tickets_publisher = tSession.createPublisher(tickets_topic);
            TopicPublisher stats_publisher = tSession.createPublisher(stats_topic);
            //@Gemini: serve metterli qui? O li passo da Manager.java?

            
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
