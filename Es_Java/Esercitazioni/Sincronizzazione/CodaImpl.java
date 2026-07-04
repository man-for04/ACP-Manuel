package Esercitazioni.Sincronizzazione;
import java.util.concurrent.locks.*;


public class CodaImpl implements Coda {
    
    private int[] buffer;
    private int testa;
    private int coda;
    private int size;

    final int DIM_BUFFER;

    //per la sincronizzazione (monitor con lock)

    private Lock lock = new ReentrantLock(true);
    private Condition cv_piena = lock.newCondition();
    private Condition cv_vuota = lock.newCondition();

    public CodaImpl(int dim_buffer){
        DIM_BUFFER=dim_buffer;
        buffer = new int[dim_buffer];
        testa=0;
        coda=0;
        size=0;
    }

    public int getSize(){
        return size;
    }

    public void inserisci(int elem){
        System.out.println("Provo a inserire...");
        lock.lock(); //mutua esclusione

        try{
            while(this.full()){
                System.out.println("Coda piena, mi metto in attesa!");
                cv_piena.await();
            }
                System.out.println("Produco..."+elem);
            buffer[coda] = elem;
            coda = (coda+1)%DIM_BUFFER;
            size++;
            cv_vuota.signal();
        }
        catch(InterruptedException e){
            System.out.print("Interrotto durante inserisci");
            e.printStackTrace();
        }
        finally{
            lock.unlock();
        }
    }

    public int preleva(){
        System.out.println("Provo a prelevare...");
        lock.lock();
        int elem=0;
        try{
            while(empty()){
                System.out.println("Mi metto in attesa...");
                cv_vuota.await();
                System.out.println("Prelevo...");
            }
            elem = buffer[testa];
            testa = (testa+1)%DIM_BUFFER;
            size--;
            cv_piena.signal();
        }
        catch(InterruptedException e){
            System.out.println("Interrotto durante preleva");
            e.printStackTrace();
        }
        finally{
            lock.unlock();
        }
        return elem;
    }

    public boolean full(){
        return size==DIM_BUFFER;
    }

    public boolean empty(){
        return size == 0;
    }

}
