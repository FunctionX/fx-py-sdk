# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/distribution/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from fxpysdk.fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from fxpysdk.fxsdk.x.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/distribution/v1beta1/tx.proto\x12\x1b\x63osmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\"\xa0\x01\n\x15MsgSetWithdrawAddress\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x32\n\x10withdraw_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x1e\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11\x64\x65legator_address\"\x1f\n\x1dMsgSetWithdrawAddressResponse\"\xa6\x01\n\x1aMsgWithdrawDelegatorReward\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x33\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x1e\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11\x64\x65legator_address\"\x81\x01\n\"MsgWithdrawDelegatorRewardResponse\x12[\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"u\n\x1eMsgWithdrawValidatorCommission\x12\x33\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x1e\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11validator_address\"\x85\x01\n&MsgWithdrawValidatorCommissionResponse\x12[\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"\xb8\x01\n\x14MsgFundCommunityPool\x12[\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12+\n\tdepositor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x16\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\tdepositor\"\x1e\n\x1cMsgFundCommunityPoolResponse2\xc8\x04\n\x03Msg\x12\x84\x01\n\x12SetWithdrawAddress\x12\x32.cosmos.distribution.v1beta1.MsgSetWithdrawAddress\x1a:.cosmos.distribution.v1beta1.MsgSetWithdrawAddressResponse\x12\x93\x01\n\x17WithdrawDelegatorReward\x12\x37.cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward\x1a?.cosmos.distribution.v1beta1.MsgWithdrawDelegatorRewardResponse\x12\x9f\x01\n\x1bWithdrawValidatorCommission\x12;.cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission\x1a\x43.cosmos.distribution.v1beta1.MsgWithdrawValidatorCommissionResponse\x12\x81\x01\n\x11\x46undCommunityPool\x12\x31.cosmos.distribution.v1beta1.MsgFundCommunityPool\x1a\x39.cosmos.distribution.v1beta1.MsgFundCommunityPoolResponseB7Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.distribution.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\250\342\036\001'
  _MSGSETWITHDRAWADDRESS.fields_by_name['delegator_address']._options = None
  _MSGSETWITHDRAWADDRESS.fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGSETWITHDRAWADDRESS.fields_by_name['withdraw_address']._options = None
  _MSGSETWITHDRAWADDRESS.fields_by_name['withdraw_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGSETWITHDRAWADDRESS._options = None
  _MSGSETWITHDRAWADDRESS._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\021delegator_address'
  _MSGWITHDRAWDELEGATORREWARD.fields_by_name['delegator_address']._options = None
  _MSGWITHDRAWDELEGATORREWARD.fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGWITHDRAWDELEGATORREWARD.fields_by_name['validator_address']._options = None
  _MSGWITHDRAWDELEGATORREWARD.fields_by_name['validator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGWITHDRAWDELEGATORREWARD._options = None
  _MSGWITHDRAWDELEGATORREWARD._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\021delegator_address'
  _MSGWITHDRAWDELEGATORREWARDRESPONSE.fields_by_name['amount']._options = None
  _MSGWITHDRAWDELEGATORREWARDRESPONSE.fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _MSGWITHDRAWVALIDATORCOMMISSION.fields_by_name['validator_address']._options = None
  _MSGWITHDRAWVALIDATORCOMMISSION.fields_by_name['validator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGWITHDRAWVALIDATORCOMMISSION._options = None
  _MSGWITHDRAWVALIDATORCOMMISSION._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\021validator_address'
  _MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE.fields_by_name['amount']._options = None
  _MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE.fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _MSGFUNDCOMMUNITYPOOL.fields_by_name['amount']._options = None
  _MSGFUNDCOMMUNITYPOOL.fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _MSGFUNDCOMMUNITYPOOL.fields_by_name['depositor']._options = None
  _MSGFUNDCOMMUNITYPOOL.fields_by_name['depositor']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGFUNDCOMMUNITYPOOL._options = None
  _MSGFUNDCOMMUNITYPOOL._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\tdepositor'
  _globals['_MSGSETWITHDRAWADDRESS']._serialized_start=176
  _globals['_MSGSETWITHDRAWADDRESS']._serialized_end=336
  _globals['_MSGSETWITHDRAWADDRESSRESPONSE']._serialized_start=338
  _globals['_MSGSETWITHDRAWADDRESSRESPONSE']._serialized_end=369
  _globals['_MSGWITHDRAWDELEGATORREWARD']._serialized_start=372
  _globals['_MSGWITHDRAWDELEGATORREWARD']._serialized_end=538
  _globals['_MSGWITHDRAWDELEGATORREWARDRESPONSE']._serialized_start=541
  _globals['_MSGWITHDRAWDELEGATORREWARDRESPONSE']._serialized_end=670
  _globals['_MSGWITHDRAWVALIDATORCOMMISSION']._serialized_start=672
  _globals['_MSGWITHDRAWVALIDATORCOMMISSION']._serialized_end=789
  _globals['_MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE']._serialized_start=792
  _globals['_MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE']._serialized_end=925
  _globals['_MSGFUNDCOMMUNITYPOOL']._serialized_start=928
  _globals['_MSGFUNDCOMMUNITYPOOL']._serialized_end=1112
  _globals['_MSGFUNDCOMMUNITYPOOLRESPONSE']._serialized_start=1114
  _globals['_MSGFUNDCOMMUNITYPOOLRESPONSE']._serialized_end=1144
  _globals['_MSG']._serialized_start=1147
  _globals['_MSG']._serialized_end=1731
# @@protoc_insertion_point(module_scope)
