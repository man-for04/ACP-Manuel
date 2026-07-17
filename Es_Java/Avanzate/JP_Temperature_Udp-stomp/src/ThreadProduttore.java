public class ThreadProduttore extends Thread{

    private float valore;
    private int tipo;
    private MiaCoda queue;

    private String[] tipi = {"LOW", "MID", "HIGH"};

    public ThreadProduttore(float valore, int tipo, MiaCoda queue) {
        this.valore = valore;
        this.tipo = tipo;
        this.queue = queue;
    }

    @Override
    public void run() {
        super.run();
        System.out.println("Thread produttore avviato");

        String to_queue = valore + "-" + tipi[tipo];

        try {
            queue.aggiungi(to_queue);
        } catch (InterruptedException e) {
            System.out.println("ERRORE INSERIMENTO NELLA CODA");
            e.printStackTrace();
        }

        System.out.println("Thread produttore terminato");

    }

    
}
