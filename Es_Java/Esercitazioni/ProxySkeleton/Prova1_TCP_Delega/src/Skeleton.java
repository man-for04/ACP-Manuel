import java.io.IOException;
import java.net.*;

public class Skeleton implements IDispatcher{
    IDispatcher delegato;
    int port;

    public Skeleton(IDispatcher del, int port){
        this.delegato = del;
        this.port=port;
    }

    public void sendCmd(int command){
        delegato.sendCmd(command);
    }

    public int getCmd(){
        return delegato.getCmd();
    }

    public void run_skeleton(){
        //Avvia il server
        try(ServerSocket s = new ServerSocket(port)){
            System.out.print("Server listening on "+s.getLocalSocketAddress()+" and port: "+s.getLocalPort());
            
            while (true) {
                Socket conn = s.accept();
                System.out.println("Ricevuta richiesta di connessione, passo a thread...");

                ServerThread td = new ServerThread(conn, this);
                td.start();

            }
        }
        catch(IOException e){
            e.printStackTrace();
        }

    }
}
