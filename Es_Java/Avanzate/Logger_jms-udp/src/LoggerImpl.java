package src;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;

public class LoggerImpl extends Skeleton{

    private PrintStream out;

    public LoggerImpl(PrintStream out){
        this.out = out;
        
    }

    @Override
    public synchronized void registraDato(int dato) {
        out.println("Saved: "+ dato);
        System.out.println("<impl> scritto su file!");
    }
    
}
