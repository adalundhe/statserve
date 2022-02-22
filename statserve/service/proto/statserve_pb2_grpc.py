# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from .statserve_pb2 import (
    StatStreamUpdate,
    StatStreamResponse,
    StatStreamQuery,
    StatStreamFieldQuery,
    StatStreamSummary,
    StatStreamFieldSummary,
    Stream
)


class StatStreamServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddStream = channel.unary_unary(
                '/StatStreamServer/AddStream',
                request_serializer=Stream.SerializeToString,
                response_deserializer=StatStreamResponse.FromString,
                )
        self.UpdateStats = channel.unary_unary(
                '/StatStreamServer/UpdateStats',
                request_serializer=StatStreamUpdate.SerializeToString,
                response_deserializer=StatStreamResponse.FromString,
                )
        self.UpdateStatsStreaming = channel.stream_stream(
                '/StatStreamServer/UpdateStatsStreaming',
                request_serializer=StatStreamUpdate.SerializeToString,
                response_deserializer=StatStreamResponse.FromString,
                )
        self.GetStreamStats = channel.unary_unary(
                '/StatStreamServer/GetStreamStats',
                request_serializer=StatStreamQuery.SerializeToString,
                response_deserializer=StatStreamSummary.FromString,
                )
        self.GetFieldStats = channel.unary_unary(
                '/StatStreamServer/GetFieldStats',
                request_serializer=StatStreamFieldQuery.SerializeToString,
                response_deserializer=StatStreamFieldSummary.FromString,
                )
        self.GetFieldStat = channel.unary_unary(
                '/StatStreamServer/GetFieldStat',
                request_serializer=StatStreamFieldQuery.SerializeToString,
                response_deserializer=StatStreamFieldSummary.FromString,
                )


class StatStreamServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateStats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateStatsStreaming(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStreamStats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFieldStats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFieldStat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StatStreamServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddStream': grpc.unary_unary_rpc_method_handler(
                    servicer.AddStream,
                    request_deserializer=Stream.FromString,
                    response_serializer=StatStreamResponse.SerializeToString,
            ),
            'UpdateStats': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateStats,
                    request_deserializer=StatStreamUpdate.FromString,
                    response_serializer=StatStreamResponse.SerializeToString,
            ),
            'UpdateStatsStreaming': grpc.stream_stream_rpc_method_handler(
                    servicer.UpdateStatsStreaming,
                    request_deserializer=StatStreamUpdate.FromString,
                    response_serializer=StatStreamResponse.SerializeToString,
            ),
            'GetStreamStats': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStreamStats,
                    request_deserializer=StatStreamQuery.FromString,
                    response_serializer=StatStreamSummary.SerializeToString,
            ),
            'GetFieldStats': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFieldStats,
                    request_deserializer=StatStreamFieldQuery.FromString,
                    response_serializer=StatStreamFieldSummary.SerializeToString,
            ),
            'GetFieldStat': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFieldStat,
                    request_deserializer=StatStreamFieldQuery.FromString,
                    response_serializer=StatStreamFieldSummary.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'StatStreamServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StatStreamServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/StatStreamServer/AddStream',
            Stream.SerializeToString,
            StatStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/StatStreamServer/UpdateStats',
            StatStreamUpdate.SerializeToString,
            StatStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateStatsStreaming(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/StatStreamServer/UpdateStatsStreaming',
            StatStreamUpdate.SerializeToString,
            StatStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStreamStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/StatStreamServer/GetStreamStats',
            StatStreamQuery.SerializeToString,
            StatStreamSummary.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFieldStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/StatStreamServer/GetFieldStats',
            StatStreamFieldQuery.SerializeToString,
            StatStreamFieldSummary.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFieldStat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/StatStreamServer/GetFieldStat',
            StatStreamFieldQuery.SerializeToString,
            StatStreamFieldSummary.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)