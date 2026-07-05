public class Client {

    public static void main(String[] args){
        final int NUMERO=5;
        int porto = Integer.parseInt(args[0]);

        ClientThread[] threads = new ClientThread[NUMERO];

        for(int i=0;i<NUMERO;i++){
            System.out.println("Sono il client, avvio i thread...");
            threads[i] = new ClientThread(porto);
            threads[i].run();
        }

        for(int i=0;i<NUMERO;i++){
            try {
                threads[i].join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("Thread "+i+" terminato!");
        }
    }
}
