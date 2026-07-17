
import java.io.IOException;
import java.net.*;
public class Proxy implements ITemperature{

    private int porto;

    public Proxy(int porto){
        this.porto=porto;
    }

    @Override
    public void temp(float valore, int tipo) {
        //Gestire la connessione
        try(DatagramSocket socket = new DatagramSocket()) {

            String msg =  Integer.toString(tipo) + '#' + Float.toString(valore);
            
            DatagramPacket to_server = new DatagramPacket(msg.getBytes(), msg.getBytes().length);
            to_server.setAddress(InetAddress.getByName("localhost"));
            to_server.setPort(porto);

            socket.send(to_server);
            
            System.out.println("Inviato al server: "+msg);


        } catch (SocketException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        
    }
    
}
