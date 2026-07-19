package mioPackage;

import static io.grpc.MethodDescriptor.generateFullMethodName;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.73.0)",
    comments = "Source: TaskManagement.proto")
@io.grpc.stub.annotations.GrpcGenerated
public final class TaskManagementGrpc {

  private TaskManagementGrpc() {}

  public static final java.lang.String SERVICE_NAME = "mioPackage.TaskManagement";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<mioPackage.TaskManagementOuterClass.msg_req_dep,
      mioPackage.TaskManagementOuterClass.msg_empty> getDeployMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "deploy",
      requestType = mioPackage.TaskManagementOuterClass.msg_req_dep.class,
      responseType = mioPackage.TaskManagementOuterClass.msg_empty.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<mioPackage.TaskManagementOuterClass.msg_req_dep,
      mioPackage.TaskManagementOuterClass.msg_empty> getDeployMethod() {
    io.grpc.MethodDescriptor<mioPackage.TaskManagementOuterClass.msg_req_dep, mioPackage.TaskManagementOuterClass.msg_empty> getDeployMethod;
    if ((getDeployMethod = TaskManagementGrpc.getDeployMethod) == null) {
      synchronized (TaskManagementGrpc.class) {
        if ((getDeployMethod = TaskManagementGrpc.getDeployMethod) == null) {
          TaskManagementGrpc.getDeployMethod = getDeployMethod =
              io.grpc.MethodDescriptor.<mioPackage.TaskManagementOuterClass.msg_req_dep, mioPackage.TaskManagementOuterClass.msg_empty>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "deploy"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  mioPackage.TaskManagementOuterClass.msg_req_dep.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  mioPackage.TaskManagementOuterClass.msg_empty.getDefaultInstance()))
              .setSchemaDescriptor(new TaskManagementMethodDescriptorSupplier("deploy"))
              .build();
        }
      }
    }
    return getDeployMethod;
  }

  private static volatile io.grpc.MethodDescriptor<mioPackage.TaskManagementOuterClass.msg_req_stop,
      mioPackage.TaskManagementOuterClass.msg_empty> getStopAllMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "stop_all",
      requestType = mioPackage.TaskManagementOuterClass.msg_req_stop.class,
      responseType = mioPackage.TaskManagementOuterClass.msg_empty.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<mioPackage.TaskManagementOuterClass.msg_req_stop,
      mioPackage.TaskManagementOuterClass.msg_empty> getStopAllMethod() {
    io.grpc.MethodDescriptor<mioPackage.TaskManagementOuterClass.msg_req_stop, mioPackage.TaskManagementOuterClass.msg_empty> getStopAllMethod;
    if ((getStopAllMethod = TaskManagementGrpc.getStopAllMethod) == null) {
      synchronized (TaskManagementGrpc.class) {
        if ((getStopAllMethod = TaskManagementGrpc.getStopAllMethod) == null) {
          TaskManagementGrpc.getStopAllMethod = getStopAllMethod =
              io.grpc.MethodDescriptor.<mioPackage.TaskManagementOuterClass.msg_req_stop, mioPackage.TaskManagementOuterClass.msg_empty>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "stop_all"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  mioPackage.TaskManagementOuterClass.msg_req_stop.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  mioPackage.TaskManagementOuterClass.msg_empty.getDefaultInstance()))
              .setSchemaDescriptor(new TaskManagementMethodDescriptorSupplier("stop_all"))
              .build();
        }
      }
    }
    return getStopAllMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static TaskManagementStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<TaskManagementStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<TaskManagementStub>() {
        @java.lang.Override
        public TaskManagementStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new TaskManagementStub(channel, callOptions);
        }
      };
    return TaskManagementStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports all types of calls on the service
   */
  public static TaskManagementBlockingV2Stub newBlockingV2Stub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<TaskManagementBlockingV2Stub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<TaskManagementBlockingV2Stub>() {
        @java.lang.Override
        public TaskManagementBlockingV2Stub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new TaskManagementBlockingV2Stub(channel, callOptions);
        }
      };
    return TaskManagementBlockingV2Stub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static TaskManagementBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<TaskManagementBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<TaskManagementBlockingStub>() {
        @java.lang.Override
        public TaskManagementBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new TaskManagementBlockingStub(channel, callOptions);
        }
      };
    return TaskManagementBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static TaskManagementFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<TaskManagementFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<TaskManagementFutureStub>() {
        @java.lang.Override
        public TaskManagementFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new TaskManagementFutureStub(channel, callOptions);
        }
      };
    return TaskManagementFutureStub.newStub(factory, channel);
  }

  /**
   */
  public interface AsyncService {

    /**
     */
    default void deploy(mioPackage.TaskManagementOuterClass.msg_req_dep request,
        io.grpc.stub.StreamObserver<mioPackage.TaskManagementOuterClass.msg_empty> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getDeployMethod(), responseObserver);
    }

    /**
     */
    default void stopAll(mioPackage.TaskManagementOuterClass.msg_req_stop request,
        io.grpc.stub.StreamObserver<mioPackage.TaskManagementOuterClass.msg_empty> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getStopAllMethod(), responseObserver);
    }
  }

  /**
   * Base class for the server implementation of the service TaskManagement.
   */
  public static abstract class TaskManagementImplBase
      implements io.grpc.BindableService, AsyncService {

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return TaskManagementGrpc.bindService(this);
    }
  }

  /**
   * A stub to allow clients to do asynchronous rpc calls to service TaskManagement.
   */
  public static final class TaskManagementStub
      extends io.grpc.stub.AbstractAsyncStub<TaskManagementStub> {
    private TaskManagementStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected TaskManagementStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new TaskManagementStub(channel, callOptions);
    }

    /**
     */
    public void deploy(mioPackage.TaskManagementOuterClass.msg_req_dep request,
        io.grpc.stub.StreamObserver<mioPackage.TaskManagementOuterClass.msg_empty> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getDeployMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void stopAll(mioPackage.TaskManagementOuterClass.msg_req_stop request,
        io.grpc.stub.StreamObserver<mioPackage.TaskManagementOuterClass.msg_empty> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getStopAllMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   * A stub to allow clients to do synchronous rpc calls to service TaskManagement.
   */
  public static final class TaskManagementBlockingV2Stub
      extends io.grpc.stub.AbstractBlockingStub<TaskManagementBlockingV2Stub> {
    private TaskManagementBlockingV2Stub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected TaskManagementBlockingV2Stub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new TaskManagementBlockingV2Stub(channel, callOptions);
    }

    /**
     */
    public mioPackage.TaskManagementOuterClass.msg_empty deploy(mioPackage.TaskManagementOuterClass.msg_req_dep request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getDeployMethod(), getCallOptions(), request);
    }

    /**
     */
    public mioPackage.TaskManagementOuterClass.msg_empty stopAll(mioPackage.TaskManagementOuterClass.msg_req_stop request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getStopAllMethod(), getCallOptions(), request);
    }
  }

  /**
   * A stub to allow clients to do limited synchronous rpc calls to service TaskManagement.
   */
  public static final class TaskManagementBlockingStub
      extends io.grpc.stub.AbstractBlockingStub<TaskManagementBlockingStub> {
    private TaskManagementBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected TaskManagementBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new TaskManagementBlockingStub(channel, callOptions);
    }

    /**
     */
    public mioPackage.TaskManagementOuterClass.msg_empty deploy(mioPackage.TaskManagementOuterClass.msg_req_dep request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getDeployMethod(), getCallOptions(), request);
    }

    /**
     */
    public mioPackage.TaskManagementOuterClass.msg_empty stopAll(mioPackage.TaskManagementOuterClass.msg_req_stop request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getStopAllMethod(), getCallOptions(), request);
    }
  }

  /**
   * A stub to allow clients to do ListenableFuture-style rpc calls to service TaskManagement.
   */
  public static final class TaskManagementFutureStub
      extends io.grpc.stub.AbstractFutureStub<TaskManagementFutureStub> {
    private TaskManagementFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected TaskManagementFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new TaskManagementFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<mioPackage.TaskManagementOuterClass.msg_empty> deploy(
        mioPackage.TaskManagementOuterClass.msg_req_dep request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getDeployMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<mioPackage.TaskManagementOuterClass.msg_empty> stopAll(
        mioPackage.TaskManagementOuterClass.msg_req_stop request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getStopAllMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_DEPLOY = 0;
  private static final int METHODID_STOP_ALL = 1;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final AsyncService serviceImpl;
    private final int methodId;

    MethodHandlers(AsyncService serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_DEPLOY:
          serviceImpl.deploy((mioPackage.TaskManagementOuterClass.msg_req_dep) request,
              (io.grpc.stub.StreamObserver<mioPackage.TaskManagementOuterClass.msg_empty>) responseObserver);
          break;
        case METHODID_STOP_ALL:
          serviceImpl.stopAll((mioPackage.TaskManagementOuterClass.msg_req_stop) request,
              (io.grpc.stub.StreamObserver<mioPackage.TaskManagementOuterClass.msg_empty>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  public static final io.grpc.ServerServiceDefinition bindService(AsyncService service) {
    return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
        .addMethod(
          getDeployMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              mioPackage.TaskManagementOuterClass.msg_req_dep,
              mioPackage.TaskManagementOuterClass.msg_empty>(
                service, METHODID_DEPLOY)))
        .addMethod(
          getStopAllMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              mioPackage.TaskManagementOuterClass.msg_req_stop,
              mioPackage.TaskManagementOuterClass.msg_empty>(
                service, METHODID_STOP_ALL)))
        .build();
  }

  private static abstract class TaskManagementBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    TaskManagementBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return mioPackage.TaskManagementOuterClass.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("TaskManagement");
    }
  }

  private static final class TaskManagementFileDescriptorSupplier
      extends TaskManagementBaseDescriptorSupplier {
    TaskManagementFileDescriptorSupplier() {}
  }

  private static final class TaskManagementMethodDescriptorSupplier
      extends TaskManagementBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final java.lang.String methodName;

    TaskManagementMethodDescriptorSupplier(java.lang.String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (TaskManagementGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new TaskManagementFileDescriptorSupplier())
              .addMethod(getDeployMethod())
              .addMethod(getStopAllMethod())
              .build();
        }
      }
    }
    return result;
  }
}
