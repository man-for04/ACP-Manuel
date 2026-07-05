import java.util.Random;

public class ClientThread extends Thread{
    private int porto;
    private Proxy proxy;

    public ClientThread(int porto){
        super();
        this.porto = porto;
        this.proxy = new Proxy(porto);
    }

    public void run(){
        Random rand = new Random();

        for(int i=0;i<3;i++){
            int tempo = rand.nextInt(3) +2;

            try {
                sleep(tempo*1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            int command = rand.nextInt(4);
            proxy.sendCmd(command);
            System.out.println("Thread: RIchiesta " + i+ " effettuata");
        }
    }

}
