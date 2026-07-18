package src;
import javax.jms.*;

public class DiskThread extends Thread{

    private MapMessage from_client;

    public DiskThread(MapMessage msg){
        this.from_client = msg;
    }

    @Override
    public void run() {
        super.run();
        System.out.println("Thread disk avviato!");

        try {
            int dato = from_client.getInt("dato");
            int porta = from_client.getInt("porta");

            System.out.println("--> <dato:"+ dato + " |porta: "+porta+">");
            Proxy proxy = new Proxy(porta); //Sono costretto a fare così, sarebbe stato più comodo passare porto come parametro della funzione ma la traccia mi vincola con la firma
            proxy.registraDato(dato);


        } catch (JMSException e) {
            System.out.println("ERRORE mapMessage!!");
            e.printStackTrace();
        }
    }
    
}
