import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class Proxy implements IDispatcher{
    //deve comunicare con il server
    int port;

    public Proxy(int port){
        this.port = port;
    }


    public void sendCmd(int command){
        try (Socket conn = new Socket("localhost",port)) {
            DataInputStream in = new DataInputStream(conn.getInputStream());
            DataOutputStream out = new DataOutputStream(conn.getOutputStream());

            System.out.print("Invio sendCmd con "+command);
            out.writeUTF("sendCmd");
            out.writeInt(command);

        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }

    public int getCmd(){
        int risultato=-1;
        try (Socket conn = new Socket("localhost",port)) {
            DataInputStream in = new DataInputStream(conn.getInputStream());
            DataOutputStream out = new DataOutputStream(conn.getOutputStream());

            System.out.print("Invio getCmd");
            out.writeUTF("getCmd");

            risultato = in.readInt();
            return risultato;

        }
        catch (IOException e) {
            e.printStackTrace();
        }
        return risultato;
        
    }
}
