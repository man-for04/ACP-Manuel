package src;

import java.io.*;

public class LoggerServer {

    public static void main(String[] args){

        try(PrintStream out = new PrintStream(new FileOutputStream("log.txt", true), true)){

            LoggerImpl server = new LoggerImpl(out);

            int port = Integer.parseInt(args[0]);
            server.run_skeleton(port);
        }
        catch(FileNotFoundException e){
            System.out.println("aiuto");
        }

    

    }

}
