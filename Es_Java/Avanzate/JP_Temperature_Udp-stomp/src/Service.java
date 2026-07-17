public class Service {
    public static void main(String[] args){
        Proxy proxy = new Proxy(Integer.parseInt(args[0]));

        System.out.println("Avvio client..");

        ThreadClient[] threads = new ThreadClient[5];

        for(int i=0;i<5;i++){
            threads[i]= new ThreadClient(proxy);
            threads[i].start();
        }

        for(int j=0;j<5;j++){
            try {
                threads[j].join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println((j+1)+" /5 Thread terminati");
        }
    }
}
