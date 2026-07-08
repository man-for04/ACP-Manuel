import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.*;

public abstract class SkeletonLogging implements ILogging{

    private int port;
    
    //Skeleton ereditarietà! Non ha rif a ServerLogging

    //Implementa la logica di connessione con socket TCP
    public SkeletonLogging(int port){
        this.port = port;
    }

    public void run_skeleton(){
        try(ServerSocket ssocket = new ServerSocket(this.port)){

            InetAddress add = ssocket.getInetAddress();
            int listport = ssocket.getLocalPort();
    
            System.out.println("Server listening on " + add +" and port: "+listport);
    
            while (true) {
                Socket conn = ssocket.accept();
                
                PrintWriter out = new PrintWriter(conn.getOutputStream(),true);
                BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
    
                String msg = in.readLine();
                System.out.println("<skel>Ricevuto dal client: "+ msg);
    
                String messaggioLog = msg.split("#")[0];
                int tipo = Integer.parseInt(msg.split("#")[1]);
                //@Gemini: qui di logica sarebbe stato più sensato lasciar perdere le variabili (tipo, messaggioLog) e passare direttamente il msg, ma dalla traccia così capisco
    
                this.log(messaggioLog, tipo);
    
                out.println("ack");
                System.out.println("<skel>Inviato al client ack");
                conn.close();
            }
        }
        catch(IOException e){
            System.out.println("ERRORE in gestione socket Skeleton");
            e.printStackTrace();

        }
        


    }

    
}
