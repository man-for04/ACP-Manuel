package Esercitazioni.Multithreading;

public class ThreadTest {
    public static void main(String[] args){
        ThreadWorker[] worker = new ThreadWorker[5];
        for(int i=0;i<5;i++){
            worker[i] = new ThreadWorker("ciaooo "+i);
            worker[i].start();
        }


        for(int i=0;i<5;i++){
            try{
                worker[i].join();
                System.out.println("Thread ("+i+") terminato");
            }
            catch(InterruptedException e){
                e.printStackTrace();
            }
        }
    }
}
