import java.io.IOException;
import java.net.DatagramSocket;
import java.net.SocketException;
import java.net.*;

public class Skeleton implements ITemperature{

    private TemperatureImpl delegate;

    public Skeleton(TemperatureImpl del){
        this.delegate=del;
    }

    @Override
    public void temp(float valore, int tipo) {
        System.out.println("delego!");
        this.delegate.temp(valore, tipo);
    }

    public void run_skeleton(){
        //Gestire comunicazione UDP con proxy
        try(DatagramSocket socket = new DatagramSocket()) {
            
            System.out.println("Server listening on "+socket.getLocalPort());
            while(true){

                byte[] buffer = new byte[60000];
    
                DatagramPacket from_server = new DatagramPacket(buffer, buffer.length);
                socket.receive(from_server);
    
                String msg = new String(buffer);
    
                System.out.println("msg: "+msg);
    
                
                int tipo = Integer.parseInt(msg.split("#")[0]);
                float valore = Float.parseFloat(msg.split("#")[1]);
                
                System.out.println("\n-->Ricevuto dal server: "+msg + "--> "+ tipo +"-"+ valore);
    
                this.delegate.temp(valore, tipo);

            }


        } catch (SocketException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
