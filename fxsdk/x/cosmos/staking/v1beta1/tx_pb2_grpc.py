# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fxsdk.x.cosmos.staking.v1beta1 import tx_pb2 as cosmos_dot_staking_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the staking Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateValidator = channel.unary_unary(
                '/cosmos.staking.v1beta1.Msg/CreateValidator',
                request_serializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgCreateValidator.SerializeToString,
                response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgCreateValidatorResponse.FromString,
                )
        self.EditValidator = channel.unary_unary(
                '/cosmos.staking.v1beta1.Msg/EditValidator',
                request_serializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgEditValidator.SerializeToString,
                response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgEditValidatorResponse.FromString,
                )
        self.Delegate = channel.unary_unary(
                '/cosmos.staking.v1beta1.Msg/Delegate',
                request_serializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgDelegate.SerializeToString,
                response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgDelegateResponse.FromString,
                )
        self.BeginRedelegate = channel.unary_unary(
                '/cosmos.staking.v1beta1.Msg/BeginRedelegate',
                request_serializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgBeginRedelegate.SerializeToString,
                response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgBeginRedelegateResponse.FromString,
                )
        self.Undelegate = channel.unary_unary(
                '/cosmos.staking.v1beta1.Msg/Undelegate',
                request_serializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgUndelegate.SerializeToString,
                response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgUndelegateResponse.FromString,
                )
        self.CancelUnbondingDelegation = channel.unary_unary(
                '/cosmos.staking.v1beta1.Msg/CancelUnbondingDelegation',
                request_serializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgCancelUnbondingDelegation.SerializeToString,
                response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgCancelUnbondingDelegationResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the staking Msg service.
    """

    def CreateValidator(self, request, context):
        """CreateValidator defines a method for creating a new validator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EditValidator(self, request, context):
        """EditValidator defines a method for editing an existing validator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delegate(self, request, context):
        """Delegate defines a method for performing a delegation of coins
        from a delegator to a validator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BeginRedelegate(self, request, context):
        """BeginRedelegate defines a method for performing a redelegation
        of coins from a delegator and source validator to a destination validator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Undelegate(self, request, context):
        """Undelegate defines a method for performing an undelegation from a
        delegate and a validator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelUnbondingDelegation(self, request, context):
        """CancelUnbondingDelegation defines a method for performing canceling the unbonding delegation
        and delegate back to previous validator.

        Since: cosmos-sdk 0.46
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateValidator': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateValidator,
                    request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgCreateValidator.FromString,
                    response_serializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgCreateValidatorResponse.SerializeToString,
            ),
            'EditValidator': grpc.unary_unary_rpc_method_handler(
                    servicer.EditValidator,
                    request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgEditValidator.FromString,
                    response_serializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgEditValidatorResponse.SerializeToString,
            ),
            'Delegate': grpc.unary_unary_rpc_method_handler(
                    servicer.Delegate,
                    request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgDelegate.FromString,
                    response_serializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgDelegateResponse.SerializeToString,
            ),
            'BeginRedelegate': grpc.unary_unary_rpc_method_handler(
                    servicer.BeginRedelegate,
                    request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgBeginRedelegate.FromString,
                    response_serializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgBeginRedelegateResponse.SerializeToString,
            ),
            'Undelegate': grpc.unary_unary_rpc_method_handler(
                    servicer.Undelegate,
                    request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgUndelegate.FromString,
                    response_serializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgUndelegateResponse.SerializeToString,
            ),
            'CancelUnbondingDelegation': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelUnbondingDelegation,
                    request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgCancelUnbondingDelegation.FromString,
                    response_serializer=cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgCancelUnbondingDelegationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosmos.staking.v1beta1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the staking Msg service.
    """

    @staticmethod
    def CreateValidator(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Msg/CreateValidator',
            cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgCreateValidator.SerializeToString,
            cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgCreateValidatorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EditValidator(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Msg/EditValidator',
            cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgEditValidator.SerializeToString,
            cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgEditValidatorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delegate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Msg/Delegate',
            cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgDelegate.SerializeToString,
            cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgDelegateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BeginRedelegate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Msg/BeginRedelegate',
            cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgBeginRedelegate.SerializeToString,
            cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgBeginRedelegateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Undelegate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Msg/Undelegate',
            cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgUndelegate.SerializeToString,
            cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgUndelegateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelUnbondingDelegation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Msg/CancelUnbondingDelegation',
            cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgCancelUnbondingDelegation.SerializeToString,
            cosmos_dot_staking_dot_v1beta1_dot_tx__pb2.MsgCancelUnbondingDelegationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
