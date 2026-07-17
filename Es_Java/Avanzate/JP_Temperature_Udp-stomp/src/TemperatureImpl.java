public class TemperatureImpl implements ITemperature{

    MiaCoda queue;

    public TemperatureImpl(MiaCoda queue){
        this.queue=queue;
    }

    @Override
    public void temp(float valore, int tipo) {
        //TODO: fai cose
        ThreadProduttore td = new ThreadProduttore(valore, tipo, queue);
        td.start();
    }
    
}
