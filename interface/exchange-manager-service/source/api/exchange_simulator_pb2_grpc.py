# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from main import exchange_simulator_pb2 as main_dot_exchange__simulator__pb2


class ExchangeSimulatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamExchangeData = channel.unary_stream(
                '/exchange.ExchangeSimulator/StreamExchangeData',
                request_serializer=main_dot_exchange__simulator__pb2.StreamRequest.SerializeToString,
                response_deserializer=main_dot_exchange__simulator__pb2.ExchangeDataUpdate.FromString,
                )
        self.Heartbeat = channel.unary_unary(
                '/exchange.ExchangeSimulator/Heartbeat',
                request_serializer=main_dot_exchange__simulator__pb2.HeartbeatRequest.SerializeToString,
                response_deserializer=main_dot_exchange__simulator__pb2.HeartbeatResponse.FromString,
                )


class ExchangeSimulatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StreamExchangeData(self, request, context):
        """Single unified stream for all exchange data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Heartbeat(self, request, context):
        """Heartbeat to verify connection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExchangeSimulatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamExchangeData': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamExchangeData,
                    request_deserializer=main_dot_exchange__simulator__pb2.StreamRequest.FromString,
                    response_serializer=main_dot_exchange__simulator__pb2.ExchangeDataUpdate.SerializeToString,
            ),
            'Heartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.Heartbeat,
                    request_deserializer=main_dot_exchange__simulator__pb2.HeartbeatRequest.FromString,
                    response_serializer=main_dot_exchange__simulator__pb2.HeartbeatResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'exchange.ExchangeSimulator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ExchangeSimulator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StreamExchangeData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/exchange.ExchangeSimulator/StreamExchangeData',
            main_dot_exchange__simulator__pb2.StreamRequest.SerializeToString,
            main_dot_exchange__simulator__pb2.ExchangeDataUpdate.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Heartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/exchange.ExchangeSimulator/Heartbeat',
            main_dot_exchange__simulator__pb2.HeartbeatRequest.SerializeToString,
            main_dot_exchange__simulator__pb2.HeartbeatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
