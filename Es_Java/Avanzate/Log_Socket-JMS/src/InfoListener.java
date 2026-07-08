import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.io.PrintWriter;

import javax.jms.*;


public class InfoListener implements MessageListener{
    PrintWriter out;

    public InfoListener(PrintWriter out){
        this.out=out;
    }

    @Override
    public void onMessage(Message message) {
        MapMessage msg = (MapMessage) message;
        try{
            //unpacking
            String messaggioLog = msg.getString("messaggioLog");
            int tipo = msg.getInt("tipo");



            if(tipo==1){
                System.out.println("Scrivo su file Info... ["+ messaggioLog +  "-"+Integer.toString(tipo)+"]");
                out.println(messaggioLog + " - "+Integer.toString(tipo));
            }
            else{
                System.out.println("No stampa in Info");
            }



        } catch (JMSException e) {
            e.printStackTrace();
        }

    }

}
