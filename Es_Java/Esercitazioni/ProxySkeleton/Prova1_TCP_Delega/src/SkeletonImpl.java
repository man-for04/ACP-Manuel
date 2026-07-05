public class SkeletonImpl implements IDispatcher{
    //deve solo implementare i servizi
    CodaImpl queue = new CodaImpl(5);

    public void sendCmd(int command){
        queue.inserisci(command);
    }

    public int getCmd(){
        return queue.preleva();
    }
}
