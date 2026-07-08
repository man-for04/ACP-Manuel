import java.io.*;
import java.net.*;

public class ProxyService implements ILogging {

    //Costruttore
    private int port;

    public ProxyService(int port) {
        this.port = port;
    }

    @Override
    public void log(String messaggioLog, int tipo) {
        //Conn a socket lato client
        try(Socket conn = new Socket("localhost", this.port)){
            System.out.println("Inviato richiesta connessione a server");
            String to_server = messaggioLog+"#"+Integer.toString(tipo);
            
            System.out.println("Sto inviando al server"+to_server);

            PrintWriter out = new PrintWriter(conn.getOutputStream(),true);
            BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));

            out.println(to_server);
            String from_server = in.readLine();

            System.out.println("Ricevuto dal server: "+from_server);
            
        }
        catch(IOException e){
            e.printStackTrace();
        }
        
    }
}
