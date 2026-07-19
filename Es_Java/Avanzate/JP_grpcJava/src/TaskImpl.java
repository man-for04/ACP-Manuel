import io.grpc.stub.StreamObserver;
import mioPackage.TaskManagementGrpc.TaskManagementImplBase;
import mioPackage.TaskManagementOuterClass.msg_empty;
import mioPackage.TaskManagementOuterClass.msg_req_dep;
import mioPackage.TaskManagementOuterClass.msg_req_stop;

public class TaskImpl extends TaskManagementImplBase{
    //Classe impl del servizio
    
    @Override
    public void deploy(msg_req_dep request, StreamObserver<msg_empty> responseObserver) {
        
        DeployThread2 td = new DeployThread2(request);
        td.start();

        msg_empty ret = msg_empty.newBuilder().build();

        responseObserver.onNext(ret);
        responseObserver.onCompleted();
    }

    @Override
    public void stopAll(msg_req_stop request, StreamObserver<msg_empty> responseObserver) {
        StopAllThread2 td = new StopAllThread2(request);
        td.start();

        msg_empty ret = msg_empty.newBuilder().build();

        responseObserver.onNext(ret);
        responseObserver.onCompleted();
    }
    
}
