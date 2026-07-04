import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args){

        try(ServerSocket s = new ServerSocket(0);){
            System.out.println("Server listening on " + s.getInetAddress()+ " and port: " + s.getLocalPort());

            while(true){
                Socket conn = s.accept();
                System.out.println("nuovo client connesso presso "+s.getInetAddress()+" e porto: "+s.getLocalPort());

                InputStream a = conn.getInputStream();
                DataInputStream in = new DataInputStream(a);

                OutputStream b = conn.getOutputStream();
                DataOutputStream out = new DataOutputStream(b);

                String from_client = in.readUTF();

                System.out.println("Client ha inviato: "+from_client);
                
                String to_client = "Ciao "+from_client;

                out.writeUTF(to_client);

                conn.close();
                System.out.println("Socket con client chiusa");

            }
        }
        catch(IOException e){
            e.printStackTrace();
        }
        

    }
}
