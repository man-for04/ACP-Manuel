
public class TemperatureServer {

    public static void main(String[] args){

        MiaCoda queue = new MiaCoda(20);
        TemperatureImpl del = new TemperatureImpl(queue);
        Skeleton ske = new Skeleton(del);

        ThreadConsumatore td = new ThreadConsumatore(queue);
        td.start();
    
        ske.run_skeleton();
    }

}
