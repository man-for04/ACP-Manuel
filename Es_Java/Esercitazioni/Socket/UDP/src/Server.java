import java.io.IOException;
import java.net.*;

public class Server {
    public static void main(String[] args){
        try(DatagramSocket conn = new DatagramSocket(0)) {

            System.out.println("Server listening on "+conn.getLocalAddress()+" and port: "+conn.getLocalPort());

            
            while(true){
                byte[] buffer = new byte[65508];
                DatagramPacket from_client = new DatagramPacket(buffer, buffer.length);
                conn.receive(from_client);
                
                int porto = from_client.getPort();
                InetAddress ip = from_client.getAddress();
    
                String text = new String(from_client.getData(), 0, from_client.getLength());
                System.out.print("Contenuto ricevuto da client: "+text);
                
                String s = "Ciao client!";
                
                DatagramPacket to_client = new DatagramPacket(s.getBytes(), s.getBytes().length);
                to_client.setPort(porto);
                to_client.setAddress(ip);
    
                conn.send(to_client);
                System.out.println("Pacchetto inviato a client!");
            }
            

        } catch (SocketException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
