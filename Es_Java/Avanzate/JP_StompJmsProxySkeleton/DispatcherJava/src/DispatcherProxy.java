import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.*;

public class DispatcherProxy implements IDispatch{

    //deve gestire la connessione e l'invio dei messaggi al server (skeleton)
    private int porto;

    
    public DispatcherProxy(int porto) {
    this.porto = porto;
    }

    @Override
    public void deposita(int valore) {

        //Creare socket connessione
        Socket c=null;
        try {
            
            c = new Socket("localhost", porto);
            

            //DataOutputStream out  = new DataOutputStream(c.getOutputStream());
            //DataInputStream in  = new DataInputStream(c.getInputStream());

            PrintWriter out = new PrintWriter(c.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(c.getInputStream()));

            String richiesta = "deposita#"+valore; 

            out.println(richiesta);

            System.out.println("<DispProxy>Ho inviato a server richiesta deposito: "+ richiesta);

            String conferma = in.readLine();
            System.out.println("Conferma deposito: "+ conferma);

            out.close();


        } catch (IOException e) {
            System.out.println("Errore creazione socket cliente");
            e.printStackTrace();
        }
        finally{
            try {
                c.close();
            } catch (IOException e) {
                System.out.println("Errore chiusura socket cliente");
                e.printStackTrace();
            }
        }
        
    }


@Override
    public int preleva() {
        //Creare socket connessione
        Socket c = null;
        try {
            
            c = new Socket("localhost", porto);

            //DataInputStream in  = new DataInputStream(c.getInputStream());
            //DataOutputStream out  = new DataOutputStream(c.getOutputStream());

            PrintWriter out = new PrintWriter(c.getOutputStream(),true);
            BufferedReader in = new BufferedReader(new InputStreamReader(c.getInputStream()));


            String richiesta = "preleva";

            
            out.println(richiesta);

            int risultato = Integer.parseInt(in.readLine());

            System.out.println("Ho ricevuto dal server risposta: "+ risultato);

            in.close();

            return risultato;


        } catch (IOException e) {
            System.out.println("Errore creazione socket cliente");
            e.printStackTrace();
        }
        finally{
            try {
                c.close();
            } catch (IOException e) {
                System.out.println("Errore chiusura socket cliente");
                e.printStackTrace();
            }
        }

        return -1;
    }

}
