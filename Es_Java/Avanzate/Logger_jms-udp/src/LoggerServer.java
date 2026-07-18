package src;

import java.io.*;

public class LoggerServer {

    public static void main(String[] args){

        try(PrintStream out = new PrintStream(new FileOutputStream("log.txt", true), true)){

            LoggerImpl server = new LoggerImpl(out);
            server.run_skeleton();
        }
        catch(FileNotFoundException e){
            System.out.println("aiuto");
        }

    

    }

}
