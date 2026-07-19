import java.io.PrintStream;

import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Message;
import javax.jms.MessageListener;

public class CPUprocessorListener implements MessageListener{

    private PrintStream out;
    

    public CPUprocessorListener(PrintStream out) {
        this.out = out;
    }


    @Override
    public void onMessage(Message message) {
        MapMessage from_server = (MapMessage) message;

        try {
            String nomeJob = from_server.getString("nomeJob");
            int tipoProcessing = from_server.getInt("tipoProcessing");
            String nomeFile = from_server.getString("nomeFile");

            System.out.println("\n--> ["+nomeJob+", "+tipoProcessing+", "+nomeFile+"]");
            this.out.println("["+nomeJob+", "+tipoProcessing+", "+nomeFile+"]\n");
            
        } catch (JMSException e) {
            e.printStackTrace();
        }

    }

}
