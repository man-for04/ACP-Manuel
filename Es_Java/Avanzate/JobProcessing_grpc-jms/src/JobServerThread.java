import javax.jms.*;


public class JobServerThread extends Thread{

    private String nomeJob;
    private int tipoProcessing;
    private String nomeFile;
    TopicSession session;
    TopicPublisher pub_cpu;
    TopicPublisher pub_gpu;

    

    public JobServerThread(String nomeJob, int tipoProcessing, String nomeFile, TopicSession session, TopicPublisher pub_cpu, TopicPublisher pub_gpu) {
        this.nomeJob = nomeJob;
        this.tipoProcessing = tipoProcessing;
        this.nomeFile = nomeFile;
        this.session = session;
        this.pub_cpu = pub_cpu;
        this.pub_gpu = pub_gpu;
    }


    @Override
    public void run() {
        System.out.println("Thread avviato!");
        //MapMessage ecc
        try {
            MapMessage to_processor = session.createMapMessage();
            to_processor.setString("nomeJob", nomeJob);
            to_processor.setInt("tipoProcessing", tipoProcessing);
            to_processor.setString("nomeFile", nomeFile);

            if(tipoProcessing == 1){
                System.out.println("<-- su topic cpu: "+nomeJob+", "+tipoProcessing+", "+nomeFile);
                pub_cpu.publish(to_processor);
            }
            else if (tipoProcessing == 2){
                System.out.println("<-- su topic gpu: "+nomeJob+", "+tipoProcessing+", "+nomeFile);
                pub_gpu.publish(to_processor);
            }
            else{
                System.out.println("ERRORE! tipoProcessing non riconosciuto: "+tipoProcessing);
            }


        } catch (JMSException e) {
            e.printStackTrace();
        }
        
    }
    
}
