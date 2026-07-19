import java.io.PrintStream;

import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Message;
import javax.jms.MessageListener;

import java.util.Random;

public class GPUprocessorListener implements MessageListener{

    private PrintStream out;
    private Random rand = new Random();
    

    public GPUprocessorListener(PrintStream out) {
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
            this.out.println("["+nomeJob+", "+tipoProcessing+", "+nomeFile+"]"+" gpu:"+rand.nextInt(1,33)+"\n");
            System.out.println("scritto");
            
        } catch (JMSException e) {
            e.printStackTrace();
        }

    }

}
