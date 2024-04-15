# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fxpysdk.fxsdk.x.cosmos.nft.v1beta1 import tx_pb2 as cosmos_dot_nft_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the nft Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Send = channel.unary_unary(
                '/cosmos.nft.v1beta1.Msg/Send',
                request_serializer=cosmos_dot_nft_dot_v1beta1_dot_tx__pb2.MsgSend.SerializeToString,
                response_deserializer=cosmos_dot_nft_dot_v1beta1_dot_tx__pb2.MsgSendResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the nft Msg service.
    """

    def Send(self, request, context):
        """Send defines a method to send a nft from one account to another account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Send': grpc.unary_unary_rpc_method_handler(
                    servicer.Send,
                    request_deserializer=cosmos_dot_nft_dot_v1beta1_dot_tx__pb2.MsgSend.FromString,
                    response_serializer=cosmos_dot_nft_dot_v1beta1_dot_tx__pb2.MsgSendResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosmos.nft.v1beta1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the nft Msg service.
    """

    @staticmethod
    def Send(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.nft.v1beta1.Msg/Send',
            cosmos_dot_nft_dot_v1beta1_dot_tx__pb2.MsgSend.SerializeToString,
            cosmos_dot_nft_dot_v1beta1_dot_tx__pb2.MsgSendResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
