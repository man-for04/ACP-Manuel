import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.io.PrintWriter;

import javax.jms.*;


public class ErrorListener implements MessageListener{
    String stringa_input;
    PrintWriter out;

    public ErrorListener(String stringa_input, PrintWriter out){
        this.stringa_input=stringa_input;
        this.out = out;

    }

    @Override
    public void onMessage(Message message) {
        MapMessage msg = (MapMessage) message;
        try {
            //unpacking
            String messaggioLog = msg.getString("messaggioLog");
            int tipo = msg.getInt("tipo");

            


            if(messaggioLog.contains("fatal") || (messaggioLog.contains("exception"))){
                System.out.println("Scrivo su file error... ["+ messaggioLog +  "-"+Integer.toString(tipo)+"]");
                out.println(messaggioLog + " - "+Integer.toString(tipo));
            }
            else{
                System.out.println("No stampa in error");
            }



        } catch (JMSException e) {
            e.printStackTrace();
        }

    }

}
