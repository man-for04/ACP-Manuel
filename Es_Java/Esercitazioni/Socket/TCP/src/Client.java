import java.net.*;

import java.io.*;


public class Client {
    public static void main(String[] args){

        int porto = Integer.parseInt(args[0]);

        try{
            Socket s = new Socket("localhost", porto);

            DataInputStream in = new DataInputStream(s.getInputStream());
            DataOutputStream out = new DataOutputStream(s.getOutputStream());


            String to_server = (String)args[1];
            System.out.println("Invio dati a server..." + to_server);

            out.writeUTF(to_server);

            String from_server = in.readUTF();

            System.out.println("Ricevuto dal server: "+ from_server);


            s.close();
            System.out.println("Addio client!");

        } catch (java.net.UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }


    }
}
