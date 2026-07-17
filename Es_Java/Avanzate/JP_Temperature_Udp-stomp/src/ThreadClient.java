import java.util.Random;

public class ThreadClient extends Thread{

    private Proxy proxy;

    public ThreadClient(Proxy proxy){
        this.proxy = proxy;
    }

    @Override
    public void run() {
        super.run();

        float valore;
        int tipo;

        Random rand = new Random();

        for (int i=0;i<10;i++){

            //generare valori
            tipo = rand.nextInt(0, 3);
            if(tipo == 0){
                //LOW
                valore = rand.nextFloat(0, 10);
            }
            else if(tipo == 1){
                //MId
                valore = rand.nextFloat(11,20);
            }
            else if(tipo == 2){
                valore = rand.nextFloat(21,30);
            }
            else{
                System.out.println("ERRORE!!");
                valore = -1;
            }

            proxy.temp(valore, tipo);

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        }
    }
    
}
