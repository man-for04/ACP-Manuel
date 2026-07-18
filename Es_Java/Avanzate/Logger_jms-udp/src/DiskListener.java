package src;
import javax.jms.*;

public class DiskListener implements MessageListener{

    @Override
    public void onMessage(Message message) {
        MapMessage from_client = (MapMessage) message;
        DiskThread td = new DiskThread(from_client);
        td.start();
    }
    
}
