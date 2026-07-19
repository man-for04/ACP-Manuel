import PackageTask.GestioneTaskGrpc.GestioneTaskImplBase;
import PackageTask.Req_string;
import PackageTask.Req_task;
import PackageTask.Res_void;
import io.grpc.stub.StreamObserver;

import java.util.Hashtable;

import javax.jms.*;
import javax.naming.*;



public class GestioneTaskImpl extends GestioneTaskImplBase{

    Topic gpuTopic;
    Topic rtTopic;
    TopicConnection tConnection;

    public GestioneTaskImpl() throws JMSException, NamingException{
        
        Hashtable<String, String> jms_properties = new Hashtable<>();
        jms_properties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        jms_properties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        jms_properties.put("topic.gpu", "gpu");
        jms_properties.put("topic.rt", "rt");

        InitialContext contesto = new InitialContext(jms_properties);
        TopicConnectionFactory tfactory = (TopicConnectionFactory) contesto.lookup("TopicConnectionFactory");

        this.gpuTopic = (Topic) contesto.lookup("gpu");
        this.rtTopic = (Topic) contesto.lookup("rt");
        this.tConnection = tfactory.createTopicConnection();
    }

    @Override
    public void deploy(Req_task request, StreamObserver<Res_void> responseObserver) {

        System.out.println("Richiesta di deploy ricevuta");
        DepolyThread td = new DepolyThread(request, this);
        td.start();
        

        Res_void risp = Res_void.newBuilder().build();
        responseObserver.onNext(risp);
        responseObserver.onCompleted();
    }

    @Override
    public void stopAll(Req_string request, StreamObserver<Res_void> responseObserver) {
        System.out.println("Richiesta di stopAll ricevuta");
        StopAllThread2 td = new StopAllThread2(request, this);
        td.start();

        Res_void risp = Res_void.newBuilder().build();
        responseObserver.onNext(risp);
        responseObserver.onCompleted();
    }
    
}
