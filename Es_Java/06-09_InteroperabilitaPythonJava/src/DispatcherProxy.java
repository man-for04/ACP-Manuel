import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.*;

import org.apache.activemq.filter.function.inListFunction;

public class DispatcherProxy implements JService{


    public DispatcherProxy(String server_address, int server_port) {
        this.server_address = server_address;
        this.server_port = server_port;
    }

    private String server_address;
    private int server_port;

    @Override
    public void desposita(int valore) {

        try{
            Socket socket = new Socket(server_address, server_port);
            //la socket java si aspetta un terminatore "\n" -> lo dovrò aggiungere in Python
            
            DataOutputStream data_out = new DataOutputStream(socket.getOutputStream());
            BufferedReader data_in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            data_out.writeUTF("deposita-" + valore);
            //mettiti in attesa delle risposta, cioè del "deposited"

            String result = data_in.readLine();
            socket.close();

        }
        catch (IOException e){
            //TODO
            e.printStackTrace();
        }

        String result = 

    }

    @Override
    public void preleva() {
        
    }

}
