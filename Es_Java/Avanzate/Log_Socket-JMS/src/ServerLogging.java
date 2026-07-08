
public class ServerLogging {
    public static void main(String[] args){
        System.out.println("Sono il server");
        int porto = Integer.parseInt(args[0]);
        LoggingImpl server = new LoggingImpl(porto);
        server.run_skeleton();
    }
}
