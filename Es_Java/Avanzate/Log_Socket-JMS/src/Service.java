import java.util.Random;

public class Service {

    public static void main(String[] args){

        int port = Integer.parseInt(args[0]);
        System.out.println("Porto: "+port);

        ProxyService proxy = new ProxyService(port);

        String[] msg_possibili_01 = {"success", "checking"};
        String[] msg_possibili_2 = {"fatal", "exception"};

        System.out.println("Ciao client!");
        
        String messaggioLog;
        int tipo;
        Random random = new Random();

        for(int i=0;i<10;i++){
            tipo = random.nextInt(3);
            if(tipo==2){
                messaggioLog = msg_possibili_2[random.nextInt(2)];
            }
            else{
                messaggioLog=msg_possibili_01[random.nextInt(2)];
            }

            proxy.log(messaggioLog, tipo);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
