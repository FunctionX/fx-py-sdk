# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fxpysdk.fxsdk.x.ibc.applications.interchain_accounts.controller.v1 import tx_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the 27-interchain-accounts/controller Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterInterchainAccount = channel.unary_unary(
                '/ibc.applications.interchain_accounts.controller.v1.Msg/RegisterInterchainAccount',
                request_serializer=ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_tx__pb2.MsgRegisterInterchainAccount.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_tx__pb2.MsgRegisterInterchainAccountResponse.FromString,
                )
        self.SendTx = channel.unary_unary(
                '/ibc.applications.interchain_accounts.controller.v1.Msg/SendTx',
                request_serializer=ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_tx__pb2.MsgSendTx.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_tx__pb2.MsgSendTxResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the 27-interchain-accounts/controller Msg service.
    """

    def RegisterInterchainAccount(self, request, context):
        """RegisterInterchainAccount defines a rpc handler for MsgRegisterInterchainAccount.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendTx(self, request, context):
        """SendTx defines a rpc handler for MsgSendTx.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterInterchainAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterInterchainAccount,
                    request_deserializer=ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_tx__pb2.MsgRegisterInterchainAccount.FromString,
                    response_serializer=ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_tx__pb2.MsgRegisterInterchainAccountResponse.SerializeToString,
            ),
            'SendTx': grpc.unary_unary_rpc_method_handler(
                    servicer.SendTx,
                    request_deserializer=ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_tx__pb2.MsgSendTx.FromString,
                    response_serializer=ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_tx__pb2.MsgSendTxResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ibc.applications.interchain_accounts.controller.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the 27-interchain-accounts/controller Msg service.
    """

    @staticmethod
    def RegisterInterchainAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.applications.interchain_accounts.controller.v1.Msg/RegisterInterchainAccount',
            ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_tx__pb2.MsgRegisterInterchainAccount.SerializeToString,
            ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_tx__pb2.MsgRegisterInterchainAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendTx(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.applications.interchain_accounts.controller.v1.Msg/SendTx',
            ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_tx__pb2.MsgSendTx.SerializeToString,
            ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_tx__pb2.MsgSendTxResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
