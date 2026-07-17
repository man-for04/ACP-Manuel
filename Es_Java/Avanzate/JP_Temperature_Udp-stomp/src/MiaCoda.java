import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class MiaCoda {

    int coda = 0;
    int dim = 0;
    int MAXSIZE;

    String[] buffer;

    //per la comunicazione
    ReentrantLock lock = new ReentrantLock();
    Condition cv_prod = lock.newCondition();
    Condition cv_cons = lock.newCondition();


    public MiaCoda(int a){
        this.MAXSIZE=a;
        this.buffer = new String[this.MAXSIZE];
    }

    private boolean is_empty(){
        return dim == 0;
    }
    private boolean is_full(){
        return dim == this.MAXSIZE;
    }

    public void aggiungi(String elem) throws InterruptedException{
        lock.lock();

        while(is_full()){
            System.out.println("<queue> prod in attesa");
            cv_prod.await();
            System.out.println("<queue> prod svegliato");
        }
        System.out.println("<queue> scrivo "+elem);
        buffer[coda] = elem;
        coda++;
        dim++;

        cv_cons.signal();

        lock.unlock();
    }

    public String preleva() throws InterruptedException{
        lock.lock();

        while(is_empty()){
            //se vuota, mi blocco
            System.out.println("<queue> cons in attesa");
            cv_cons.await();
            System.out.println("<queue> cons svegliato");

        }
        coda--;
        String elem = buffer[coda];
        System.out.println("<queue> prelevato "+elem);
        dim--;

        cv_prod.signal();

        lock.unlock();

        return elem;
    }
}
