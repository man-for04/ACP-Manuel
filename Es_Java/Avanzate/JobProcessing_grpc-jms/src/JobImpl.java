import java.util.Hashtable;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

import javax.jms.JMSException;
import javax.jms.Session;
import javax.jms.Topic;
import javax.jms.TopicConnection;
import javax.jms.TopicConnectionFactory;
import javax.jms.TopicPublisher;
import javax.jms.TopicSession;
import javax.naming.InitialContext;
import javax.naming.NamingException;

import io.grpc.stub.StreamObserver;
import mioPackage.IJobUser.msg_empty;
import mioPackage.IJobUser.msg_req;
import mioPackage.JobsGrpc.JobsImplBase;

public class JobImpl extends JobsImplBase{

    private Lock lucchetto = new ReentrantLock();


    @Override
    public void jobReq(msg_req request, StreamObserver<msg_empty> responseObserver) {

        this.lucchetto.lock(); //è stato richiesto, anche se non ha molto senso
        
        String nomeJob = request.getNomeJob();
        int tipoProcessing = request.getTipoProcessing();
        String nomeFile = request.getNomeFile();

        System.out.println("--> ricevuto ["+nomeJob+", "+tipoProcessing+", "+nomeFile+"]");

        //setup jms
        Hashtable<String, String> jms_properties = new Hashtable<>();
        /*"java.naming.factory.initial" -> "org.apache.activemq.jndi.ActiveMQInitialContextFactory"
        "java.naming.provider.url" -> "tcp://127.0.0.1:61616" */
        jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        jms_properties.put("topic.gpu", "gpu");
        jms_properties.put("topic.cpu", "cpu");

        InitialContext contesto;
        try {
            contesto = new InitialContext(jms_properties);
            TopicConnectionFactory factory = (TopicConnectionFactory) contesto.lookup("TopicConnectionFactory");
            Topic topic_gpu = (Topic) contesto.lookup("gpu");
            Topic topic_cpu = (Topic) contesto.lookup("cpu");
    
            TopicConnection connection = (TopicConnection) factory.createTopicConnection();
            TopicSession session = (TopicSession) connection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
            TopicPublisher pub_gpu = session.createPublisher(topic_gpu);
            TopicPublisher pub_cpu = session.createPublisher(topic_cpu);
    
            JobServerThread td = new JobServerThread(nomeJob, tipoProcessing, nomeFile, session, pub_cpu, pub_gpu);
            td.start();

        } catch (NamingException | JMSException e) {
            
            e.printStackTrace();
        }

        msg_empty msg = msg_empty.newBuilder().build();
        responseObserver.onNext(msg);
        responseObserver.onCompleted();
        //@Gemini: che succede se qui invece non avessi ritornato nulla?

        this.lucchetto.unlock();

    }

}
