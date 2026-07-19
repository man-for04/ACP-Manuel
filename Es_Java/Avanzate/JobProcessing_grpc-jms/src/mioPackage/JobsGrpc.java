package mioPackage;

import static io.grpc.MethodDescriptor.generateFullMethodName;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.73.0)",
    comments = "Source: IJobUser.proto")
@io.grpc.stub.annotations.GrpcGenerated
public final class JobsGrpc {

  private JobsGrpc() {}

  public static final java.lang.String SERVICE_NAME = "mioPackage.Jobs";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<mioPackage.IJobUser.msg_req,
      mioPackage.IJobUser.msg_empty> getJobReqMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "job_req",
      requestType = mioPackage.IJobUser.msg_req.class,
      responseType = mioPackage.IJobUser.msg_empty.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<mioPackage.IJobUser.msg_req,
      mioPackage.IJobUser.msg_empty> getJobReqMethod() {
    io.grpc.MethodDescriptor<mioPackage.IJobUser.msg_req, mioPackage.IJobUser.msg_empty> getJobReqMethod;
    if ((getJobReqMethod = JobsGrpc.getJobReqMethod) == null) {
      synchronized (JobsGrpc.class) {
        if ((getJobReqMethod = JobsGrpc.getJobReqMethod) == null) {
          JobsGrpc.getJobReqMethod = getJobReqMethod =
              io.grpc.MethodDescriptor.<mioPackage.IJobUser.msg_req, mioPackage.IJobUser.msg_empty>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "job_req"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  mioPackage.IJobUser.msg_req.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  mioPackage.IJobUser.msg_empty.getDefaultInstance()))
              .setSchemaDescriptor(new JobsMethodDescriptorSupplier("job_req"))
              .build();
        }
      }
    }
    return getJobReqMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static JobsStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<JobsStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<JobsStub>() {
        @java.lang.Override
        public JobsStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new JobsStub(channel, callOptions);
        }
      };
    return JobsStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports all types of calls on the service
   */
  public static JobsBlockingV2Stub newBlockingV2Stub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<JobsBlockingV2Stub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<JobsBlockingV2Stub>() {
        @java.lang.Override
        public JobsBlockingV2Stub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new JobsBlockingV2Stub(channel, callOptions);
        }
      };
    return JobsBlockingV2Stub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static JobsBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<JobsBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<JobsBlockingStub>() {
        @java.lang.Override
        public JobsBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new JobsBlockingStub(channel, callOptions);
        }
      };
    return JobsBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static JobsFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<JobsFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<JobsFutureStub>() {
        @java.lang.Override
        public JobsFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new JobsFutureStub(channel, callOptions);
        }
      };
    return JobsFutureStub.newStub(factory, channel);
  }

  /**
   */
  public interface AsyncService {

    /**
     */
    default void jobReq(mioPackage.IJobUser.msg_req request,
        io.grpc.stub.StreamObserver<mioPackage.IJobUser.msg_empty> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getJobReqMethod(), responseObserver);
    }
  }

  /**
   * Base class for the server implementation of the service Jobs.
   */
  public static abstract class JobsImplBase
      implements io.grpc.BindableService, AsyncService {

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return JobsGrpc.bindService(this);
    }
  }

  /**
   * A stub to allow clients to do asynchronous rpc calls to service Jobs.
   */
  public static final class JobsStub
      extends io.grpc.stub.AbstractAsyncStub<JobsStub> {
    private JobsStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected JobsStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new JobsStub(channel, callOptions);
    }

    /**
     */
    public void jobReq(mioPackage.IJobUser.msg_req request,
        io.grpc.stub.StreamObserver<mioPackage.IJobUser.msg_empty> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getJobReqMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   * A stub to allow clients to do synchronous rpc calls to service Jobs.
   */
  public static final class JobsBlockingV2Stub
      extends io.grpc.stub.AbstractBlockingStub<JobsBlockingV2Stub> {
    private JobsBlockingV2Stub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected JobsBlockingV2Stub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new JobsBlockingV2Stub(channel, callOptions);
    }

    /**
     */
    public mioPackage.IJobUser.msg_empty jobReq(mioPackage.IJobUser.msg_req request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getJobReqMethod(), getCallOptions(), request);
    }
  }

  /**
   * A stub to allow clients to do limited synchronous rpc calls to service Jobs.
   */
  public static final class JobsBlockingStub
      extends io.grpc.stub.AbstractBlockingStub<JobsBlockingStub> {
    private JobsBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected JobsBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new JobsBlockingStub(channel, callOptions);
    }

    /**
     */
    public mioPackage.IJobUser.msg_empty jobReq(mioPackage.IJobUser.msg_req request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getJobReqMethod(), getCallOptions(), request);
    }
  }

  /**
   * A stub to allow clients to do ListenableFuture-style rpc calls to service Jobs.
   */
  public static final class JobsFutureStub
      extends io.grpc.stub.AbstractFutureStub<JobsFutureStub> {
    private JobsFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected JobsFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new JobsFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<mioPackage.IJobUser.msg_empty> jobReq(
        mioPackage.IJobUser.msg_req request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getJobReqMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_JOB_REQ = 0;

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
        case METHODID_JOB_REQ:
          serviceImpl.jobReq((mioPackage.IJobUser.msg_req) request,
              (io.grpc.stub.StreamObserver<mioPackage.IJobUser.msg_empty>) responseObserver);
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
          getJobReqMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              mioPackage.IJobUser.msg_req,
              mioPackage.IJobUser.msg_empty>(
                service, METHODID_JOB_REQ)))
        .build();
  }

  private static abstract class JobsBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    JobsBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return mioPackage.IJobUser.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("Jobs");
    }
  }

  private static final class JobsFileDescriptorSupplier
      extends JobsBaseDescriptorSupplier {
    JobsFileDescriptorSupplier() {}
  }

  private static final class JobsMethodDescriptorSupplier
      extends JobsBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final java.lang.String methodName;

    JobsMethodDescriptorSupplier(java.lang.String methodName) {
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
      synchronized (JobsGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new JobsFileDescriptorSupplier())
              .addMethod(getJobReqMethod())
              .build();
        }
      }
    }
    return result;
  }
}
