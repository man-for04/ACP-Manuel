package Esercitazioni.Multithreading;

public class ThreadWorker extends Thread{
    String message;
    public ThreadWorker(String message){
        super();
        this.message=message;
    }

    @Override
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
