import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class ServerThread extends Thread{
    Socket conn;
    IDispatcher ske;
    public ServerThread(Socket conn, IDispatcher ske){
        super();
        this.conn=conn;
        this.ske=ske;
    }

    public void run(){
        //Comportamento del thread
        
        try {
            DataInputStream in = new DataInputStream(conn.getInputStream());
            DataOutputStream out = new DataOutputStream(conn.getOutputStream());
            
            String method = in.readUTF();

            if(method.equals("sendCmd")){
                System.out.println("Richiesta di sendCmd");
                int command = in.readInt();
                ske.sendCmd(command);
                out.writeUTF("ack");

            }
            else if(method.equals("getCmd")){
                System.out.println("Richiesta di getCmd");
                int x=ske.getCmd();
                out.writeInt(x);
            }
            else{
                System.out.println("metodo non riconosciuto!");
                out.writeUTF("failed");
            }

            conn.close();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
