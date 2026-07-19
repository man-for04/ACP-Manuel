import java.util.Hashtable;

import javax.jms.*;
import javax.naming.InitialContext;
import javax.naming.NamingException;

import java.util.Random;

public class Client {

    public static void main(String[] args){

        //setup jms
        Hashtable<String, String> jms_properties = new Hashtable<>();
        /*"java.naming.factory.initial" -> "org.apache.activemq.jndi.ActiveMQInitialContextFactory"
        "java.naming.provider.url" -> "tcp://127.0.0.1:61616" */
        jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        jms_properties.put("topic.data", "data");

        try {
            InitialContext contesto = new InitialContext(jms_properties);

            TopicConnectionFactory factory = (TopicConnectionFactory) contesto.lookup("TopicConnectionFactory");
            Topic data_topic = (Topic) contesto.lookup("data");

            TopicConnection connection = factory.createTopicConnection();

            TopicSession session = connection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);

            TopicPublisher pub = session.createPublisher(data_topic);

            MapMessage to_extractor = session.createMapMessage();

            String type = args[0];
            System.out.println("Tipo di richiesta: "+type);

            to_extractor.setString("type", type);
            int value=-1;
            Random rand = new Random();

            //genera 20 richieste attentendo 2 sec

            if(type.equals("temperature")){


                for(int i=0;i<20;i++){
                    value = rand.nextInt(0, 101);

                    System.out.println("<-- ["+type+"-"+value+"]");
                    to_extractor.setInt("value", value);

                    pub.publish(to_extractor);
                    System.out.println("inviato\n");

                    Thread.sleep(1000);
                }


            }
            else if(type.equals("pressure")){

                for(int i=0;i<20;i++){
                    value = rand.nextInt(1000, 1050);

                    System.out.println("<-- ["+type+"-"+value+"]");
                    to_extractor.setInt("value", value);

                    pub.publish(to_extractor);
                    System.out.println("inviato\n");

                    Thread.sleep(1000);
                }

            }
            else{
                System.out.println("ERRORE! type inserito da terminale non valido");
            }

            pub.close();
            session.close();
            connection.close();


        } catch (NamingException | JMSException | InterruptedException e) {
            e.printStackTrace();
        }
        


    }
}
