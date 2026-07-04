import java.io.IOException;
import java.net.*;

public class Server {
    public static void main(String[] args){
        try(DatagramSocket conn = new DatagramSocket(0)) {

            System.out.println("Server listening on "+conn.getInetAddress()+" and port: "+conn.getLocalPort());

            byte[] buffer = new byte[4000];

            DatagramPacket from_client = new DatagramPacket(buffer, buffer.length);
            conn.receive(from_client);

            //TODO: Continua con risposta

        } catch (SocketException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
