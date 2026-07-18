package src;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;

public abstract class Skeleton implements ILogger{

    //Il metodo verrà ridefinito da LoggerImpl

    //Devo occuparmi di effettuare la connessione

    public void run_skeleton(){
        try(DatagramSocket conn = new DatagramSocket(0)){
            
            byte[] buffer = new byte[60000];
            DatagramPacket from_disk = new DatagramPacket(buffer, buffer.length);
    
            System.out.println("LoggerServer in ascolto su: "+conn.getLocalAddress()+"+ port: "+conn.getLocalPort());

            while(true){
        
                conn.receive(from_disk);
                
                String msg = new String(from_disk.getData(), 0, from_disk.getData().length).trim();
                System.out.println("--> Messaggio in formato stringa ricevuto: "+msg);
                int dato = Integer.parseInt(msg);
        
                System.out.println("--> <Skeleton> ricevuto dato: "+dato);
        
                this.registraDato(dato);
            }
            

        }
        catch(IOException e){
            e.printStackTrace();
        }
    }
    

}
