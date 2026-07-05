import java.io.IOException;
import java.net.*;

public class Client {
    public static void main(String[] args){
        
        try (DatagramSocket conn = new DatagramSocket()) {

            System.out.println("Sono client e devo inviare pacchetto a server!");
            
            int porto =  Integer.parseInt(args[0]);
            String s = args[1];
            
            DatagramPacket to_server = new DatagramPacket(s.getBytes(), s.getBytes().length, InetAddress.getByName("localhost"), porto);
            conn.send(to_server);
            System.out.print("Ho inviato <"+s+"> al server");

            byte[] buf = new byte[60000];
            DatagramPacket from_server = new DatagramPacket(buf, buf.length);
            conn.receive(from_server);
            String text = new String(from_server.getData(), 0, from_server.getLength());

            System.out.print("Ricevuto dal server: "+text);
            
            conn.close();




        } catch (SocketException e) {
            e.printStackTrace();
        }
        catch (UnknownHostException e) {
            e.printStackTrace();
        }
        catch(IOException e){
            e.printStackTrace();
        }
        
    }
}
