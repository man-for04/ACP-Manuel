package PackageTask;

import static io.grpc.MethodDescriptor.generateFullMethodName;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.73.0)",
    comments = "Source: GestioneTask.proto")
@io.grpc.stub.annotations.GrpcGenerated
public final class GestioneTaskGrpc {

  private GestioneTaskGrpc() {}

  public static final java.lang.String SERVICE_NAME = "PackageTask.GestioneTask";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<PackageTask.Req_task,
      PackageTask.Res_void> getDeployMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "deploy",
      requestType = PackageTask.Req_task.class,
      responseType = PackageTask.Res_void.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<PackageTask.Req_task,
      PackageTask.Res_void> getDeployMethod() {
    io.grpc.MethodDescriptor<PackageTask.Req_task, PackageTask.Res_void> getDeployMethod;
    if ((getDeployMethod = GestioneTaskGrpc.getDeployMethod) == null) {
      synchronized (GestioneTaskGrpc.class) {
        if ((getDeployMethod = GestioneTaskGrpc.getDeployMethod) == null) {
          GestioneTaskGrpc.getDeployMethod = getDeployMethod =
              io.grpc.MethodDescriptor.<PackageTask.Req_task, PackageTask.Res_void>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "deploy"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  PackageTask.Req_task.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  PackageTask.Res_void.getDefaultInstance()))
              .setSchemaDescriptor(new GestioneTaskMethodDescriptorSupplier("deploy"))
              .build();
        }
      }
    }
    return getDeployMethod;
  }

  private static volatile io.grpc.MethodDescriptor<PackageTask.Req_string,
      PackageTask.Res_void> getStopAllMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "stop_all",
      requestType = PackageTask.Req_string.class,
      responseType = PackageTask.Res_void.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<PackageTask.Req_string,
      PackageTask.Res_void> getStopAllMethod() {
    io.grpc.MethodDescriptor<PackageTask.Req_string, PackageTask.Res_void> getStopAllMethod;
    if ((getStopAllMethod = GestioneTaskGrpc.getStopAllMethod) == null) {
      synchronized (GestioneTaskGrpc.class) {
        if ((getStopAllMethod = GestioneTaskGrpc.getStopAllMethod) == null) {
          GestioneTaskGrpc.getStopAllMethod = getStopAllMethod =
              io.grpc.MethodDescriptor.<PackageTask.Req_string, PackageTask.Res_void>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "stop_all"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  PackageTask.Req_string.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  PackageTask.Res_void.getDefaultInstance()))
              .setSchemaDescriptor(new GestioneTaskMethodDescriptorSupplier("stop_all"))
              .build();
        }
      }
    }
    return getStopAllMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static GestioneTaskStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<GestioneTaskStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<GestioneTaskStub>() {
        @java.lang.Override
        public GestioneTaskStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new GestioneTaskStub(channel, callOptions);
        }
      };
    return GestioneTaskStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports all types of calls on the service
   */
  public static GestioneTaskBlockingV2Stub newBlockingV2Stub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<GestioneTaskBlockingV2Stub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<GestioneTaskBlockingV2Stub>() {
        @java.lang.Override
        public GestioneTaskBlockingV2Stub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new GestioneTaskBlockingV2Stub(channel, callOptions);
        }
      };
    return GestioneTaskBlockingV2Stub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static GestioneTaskBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<GestioneTaskBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<GestioneTaskBlockingStub>() {
        @java.lang.Override
        public GestioneTaskBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new GestioneTaskBlockingStub(channel, callOptions);
        }
      };
    return GestioneTaskBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static GestioneTaskFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<GestioneTaskFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<GestioneTaskFutureStub>() {
        @java.lang.Override
        public GestioneTaskFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new GestioneTaskFutureStub(channel, callOptions);
        }
      };
    return GestioneTaskFutureStub.newStub(factory, channel);
  }

  /**
   */
  public interface AsyncService {

    /**
     */
    default void deploy(PackageTask.Req_task request,
        io.grpc.stub.StreamObserver<PackageTask.Res_void> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getDeployMethod(), responseObserver);
    }

    /**
     */
    default void stopAll(PackageTask.Req_string request,
        io.grpc.stub.StreamObserver<PackageTask.Res_void> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getStopAllMethod(), responseObserver);
    }
  }

  /**
   * Base class for the server implementation of the service GestioneTask.
   */
  public static abstract class GestioneTaskImplBase
      implements io.grpc.BindableService, AsyncService {

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return GestioneTaskGrpc.bindService(this);
    }
  }

  /**
   * A stub to allow clients to do asynchronous rpc calls to service GestioneTask.
   */
  public static final class GestioneTaskStub
      extends io.grpc.stub.AbstractAsyncStub<GestioneTaskStub> {
    private GestioneTaskStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GestioneTaskStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new GestioneTaskStub(channel, callOptions);
    }

    /**
     */
    public void deploy(PackageTask.Req_task request,
        io.grpc.stub.StreamObserver<PackageTask.Res_void> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getDeployMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void stopAll(PackageTask.Req_string request,
        io.grpc.stub.StreamObserver<PackageTask.Res_void> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getStopAllMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   * A stub to allow clients to do synchronous rpc calls to service GestioneTask.
   */
  public static final class GestioneTaskBlockingV2Stub
      extends io.grpc.stub.AbstractBlockingStub<GestioneTaskBlockingV2Stub> {
    private GestioneTaskBlockingV2Stub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GestioneTaskBlockingV2Stub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new GestioneTaskBlockingV2Stub(channel, callOptions);
    }

    /**
     */
    public PackageTask.Res_void deploy(PackageTask.Req_task request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getDeployMethod(), getCallOptions(), request);
    }

    /**
     */
    public PackageTask.Res_void stopAll(PackageTask.Req_string request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getStopAllMethod(), getCallOptions(), request);
    }
  }

  /**
   * A stub to allow clients to do limited synchronous rpc calls to service GestioneTask.
   */
  public static final class GestioneTaskBlockingStub
      extends io.grpc.stub.AbstractBlockingStub<GestioneTaskBlockingStub> {
    private GestioneTaskBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GestioneTaskBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new GestioneTaskBlockingStub(channel, callOptions);
    }

    /**
     */
    public PackageTask.Res_void deploy(PackageTask.Req_task request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getDeployMethod(), getCallOptions(), request);
    }

    /**
     */
    public PackageTask.Res_void stopAll(PackageTask.Req_string request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getStopAllMethod(), getCallOptions(), request);
    }
  }

  /**
   * A stub to allow clients to do ListenableFuture-style rpc calls to service GestioneTask.
   */
  public static final class GestioneTaskFutureStub
      extends io.grpc.stub.AbstractFutureStub<GestioneTaskFutureStub> {
    private GestioneTaskFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GestioneTaskFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new GestioneTaskFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<PackageTask.Res_void> deploy(
        PackageTask.Req_task request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getDeployMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<PackageTask.Res_void> stopAll(
        PackageTask.Req_string request) {
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
          serviceImpl.deploy((PackageTask.Req_task) request,
              (io.grpc.stub.StreamObserver<PackageTask.Res_void>) responseObserver);
          break;
        case METHODID_STOP_ALL:
          serviceImpl.stopAll((PackageTask.Req_string) request,
              (io.grpc.stub.StreamObserver<PackageTask.Res_void>) responseObserver);
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
              PackageTask.Req_task,
              PackageTask.Res_void>(
                service, METHODID_DEPLOY)))
        .addMethod(
          getStopAllMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              PackageTask.Req_string,
              PackageTask.Res_void>(
                service, METHODID_STOP_ALL)))
        .build();
  }

  private static abstract class GestioneTaskBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    GestioneTaskBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return PackageTask.GestioneTaskOuterClass.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("GestioneTask");
    }
  }

  private static final class GestioneTaskFileDescriptorSupplier
      extends GestioneTaskBaseDescriptorSupplier {
    GestioneTaskFileDescriptorSupplier() {}
  }

  private static final class GestioneTaskMethodDescriptorSupplier
      extends GestioneTaskBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final java.lang.String methodName;

    GestioneTaskMethodDescriptorSupplier(java.lang.String methodName) {
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
      synchronized (GestioneTaskGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new GestioneTaskFileDescriptorSupplier())
              .addMethod(getDeployMethod())
              .addMethod(getStopAllMethod())
              .build();
        }
      }
    }
    return result;
  }
}
