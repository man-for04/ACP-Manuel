package src;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;


public class Proxy implements ILogger{

    private int porta;
    public Proxy(int port){
        this.porta = port;
    }

    @Override
    public void registraDato(int dato) {

        //Gestire connessione
        try(DatagramSocket conn = new DatagramSocket()) {

            byte[] buffer = Integer.toString(dato).getBytes();

            DatagramPacket to_logger = new DatagramPacket(buffer, buffer.length);
            to_logger.setAddress(InetAddress.getByName("localhost"));
            to_logger.setPort(this.porta);

            System.out.println("<-- <Proxy> invio pacchetto "+ this.porta +", "+ dato);
            conn.send(to_logger);

        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        };
    }
    
}
