//package Esercitazioni.Multithreading;

public class MioThread implements Runnable{
    private String message;

    public MioThread(String message){
        this.message=message;
    }

    public void run(){
        System.out.println(Thread.currentThread().getName() + "message: "+message);
        try{
            Thread.sleep(1000);
        }
        catch(InterruptedException e){
            e.printStackTrace();
        };
        System.out.println("Thread terminato!");
    }
}
