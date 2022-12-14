# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from x.fx.other import query_pb2 as fx_dot_other_dot_query__pb2


class QueryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GasPrice = channel.unary_unary(
                '/fx.other.Query/GasPrice',
                request_serializer=fx_dot_other_dot_query__pb2.GasPriceRequest.SerializeToString,
                response_deserializer=fx_dot_other_dot_query__pb2.GasPriceResponse.FromString,
                )


class QueryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GasPrice(self, request, context):
        """Deprecated
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GasPrice': grpc.unary_unary_rpc_method_handler(
                    servicer.GasPrice,
                    request_deserializer=fx_dot_other_dot_query__pb2.GasPriceRequest.FromString,
                    response_serializer=fx_dot_other_dot_query__pb2.GasPriceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fx.other.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GasPrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.other.Query/GasPrice',
            fx_dot_other_dot_query__pb2.GasPriceRequest.SerializeToString,
            fx_dot_other_dot_query__pb2.GasPriceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
