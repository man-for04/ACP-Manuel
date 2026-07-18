import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;

import javax.jms.*;

public class ListenerCPU implements MessageListener{

    PrintStream out;

    public ListenerCPU() throws FileNotFoundException{
        this.out = new PrintStream(new FileOutputStream("CPU.txt", true), true);
    }


    @Override
    public void onMessage(Message message) {
        //alla ricezione su topic CPU stampa il task e scrivi su CPU.txt
        TextMessage msg = (TextMessage) message;
        try {
            String task = msg.getText();

            System.out.println("--> <CPU> ricevuto: "+ task);
            out.println(task);

        } catch (JMSException e) {
            e.printStackTrace();
        }
    }

}
