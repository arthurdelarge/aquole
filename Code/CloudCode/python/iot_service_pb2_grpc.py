# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import iot_service_pb2 as iot__service__pb2


class IoTServiceStub(object):
    """The acceleration service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayAcceleration = channel.unary_unary(
                '/iot_service.IoTService/SayAcceleration',
                request_serializer=iot__service__pb2.AccelerationRequest.SerializeToString,
                response_deserializer=iot__service__pb2.AccelerationReply.FromString,
                )
        self.CreateUser = channel.unary_unary(
                '/iot_service.IoTService/CreateUser',
                request_serializer=iot__service__pb2.UserRequest.SerializeToString,
                response_deserializer=iot__service__pb2.StatusReply.FromString,
                )
        self.UserLogin = channel.unary_unary(
                '/iot_service.IoTService/UserLogin',
                request_serializer=iot__service__pb2.LoginRequest.SerializeToString,
                response_deserializer=iot__service__pb2.LoginReply.FromString,
                )
        self.SayLightLevel = channel.unary_unary(
                '/iot_service.IoTService/SayLightLevel',
                request_serializer=iot__service__pb2.LightLevelRequest.SerializeToString,
                response_deserializer=iot__service__pb2.LightLevelReply.FromString,
                )


class IoTServiceServicer(object):
    """The acceleration service definition.
    """

    def SayAcceleration(self, request, context):
        """Responds with a acceleration measurement
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UserLogin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayLightLevel(self, request, context):
        """Responds with the current reading of a given light sensor
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IoTServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayAcceleration': grpc.unary_unary_rpc_method_handler(
                    servicer.SayAcceleration,
                    request_deserializer=iot__service__pb2.AccelerationRequest.FromString,
                    response_serializer=iot__service__pb2.AccelerationReply.SerializeToString,
            ),
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=iot__service__pb2.UserRequest.FromString,
                    response_serializer=iot__service__pb2.StatusReply.SerializeToString,
            ),
            'UserLogin': grpc.unary_unary_rpc_method_handler(
                    servicer.UserLogin,
                    request_deserializer=iot__service__pb2.LoginRequest.FromString,
                    response_serializer=iot__service__pb2.LoginReply.SerializeToString,
            ),
            'SayLightLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.SayLightLevel,
                    request_deserializer=iot__service__pb2.LightLevelRequest.FromString,
                    response_serializer=iot__service__pb2.LightLevelReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'iot_service.IoTService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IoTService(object):
    """The acceleration service definition.
    """

    @staticmethod
    def SayAcceleration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iot_service.IoTService/SayAcceleration',
            iot__service__pb2.AccelerationRequest.SerializeToString,
            iot__service__pb2.AccelerationReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iot_service.IoTService/CreateUser',
            iot__service__pb2.UserRequest.SerializeToString,
            iot__service__pb2.StatusReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UserLogin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iot_service.IoTService/UserLogin',
            iot__service__pb2.LoginRequest.SerializeToString,
            iot__service__pb2.LoginReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayLightLevel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iot_service.IoTService/SayLightLevel',
            iot__service__pb2.LightLevelRequest.SerializeToString,
            iot__service__pb2.LightLevelReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
