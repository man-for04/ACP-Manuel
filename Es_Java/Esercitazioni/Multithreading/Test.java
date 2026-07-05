package Esercitazioni.Multithreading;

public class Test {
    public static void main(String[] args){
        
        Thread threads [] = new Thread[5];
        for(int i=0;i<5;i++){
            MioThread td = new MioThread("ciao "+i);
            threads[i] = new Thread(td);
            threads[i].start();
        }

        for(int i=0;i<5;i++){
            try{
                threads[i].join();
            }
            catch (InterruptedException e){
                e.printStackTrace();
            }
        }
    }
}
