import java.io.FileOutputStream;
import java.io.PrintStream;

public class Actuator {
    
    public static void main(String[] args){
        int porto = Integer.parseInt(args[0]);

        Proxy proxy = new Proxy(porto);
        PrintStream outStream=null;

        try{
            FileOutputStream out = new FileOutputStream("./cmdlog.txt");
            outStream = new PrintStream(out);

            while(true){
                int x =proxy.getCmd();
                System.out.println("<Actuator> ho ottenuto "+x);
                outStream.println(x);
    
                Thread.sleep(1000);
            }
        }
        catch(Exception e){
            e.printStackTrace();
        }
        finally{
            outStream.close();
        }
        

    }

}
