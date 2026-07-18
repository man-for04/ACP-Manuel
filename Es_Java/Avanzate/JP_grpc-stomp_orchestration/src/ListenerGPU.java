import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;

import javax.jms.*;

public class ListenerGPU implements MessageListener{

    PrintStream out;

    public ListenerGPU() throws FileNotFoundException{
        this.out = new PrintStream(new FileOutputStream("GPU.txt", true), true);
    }


    @Override
    public void onMessage(Message message) {
        //alla ricezione su topic GPU stampa il task e scrivi su GPU.txt
        TextMessage msg = (TextMessage) message;
        try {
            String task = msg.getText();

            System.out.println("--> <GPU> ricevuto: "+ task);
            out.println(task);

        } catch (JMSException e) {
            e.printStackTrace();
        }
    }
    
}
