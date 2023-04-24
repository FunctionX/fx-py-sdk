# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/crosschain/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from x.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from x.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from x.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from x.fx.crosschain.v1 import types_pb2 as fx_dot_crosschain_dot_v1_dot_types__pb2
from x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x66x/crosschain/v1/tx.proto\x12\x18\x66x.gravity.crosschain.v1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1c\x66x/crosschain/v1/types.proto\x1a\x14gogoproto/gogo.proto\"\xc5\x01\n\x0fMsgBondedOracle\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12\x16\n\x0eoracle_address\x18\x02 \x01(\t\x12\x17\n\x0f\x62ridger_address\x18\x03 \x01(\t\x12\x18\n\x10\x65xternal_address\x18\x04 \x01(\t\x12\x19\n\x11validator_address\x18\x05 \x01(\t\x12\x38\n\x0f\x64\x65legate_amount\x18\x06 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\x19\n\x17MsgBondedOracleResponse\"m\n\x0eMsgAddDelegate\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12\x16\n\x0eoracle_address\x18\x02 \x01(\t\x12/\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\x18\n\x16MsgAddDelegateResponse\"V\n\rMsgReDelegate\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12\x16\n\x0eoracle_address\x18\x02 \x01(\t\x12\x19\n\x11validator_address\x18\x03 \x01(\t\"\x17\n\x15MsgReDelegateResponse\"U\n\x0eMsgEditBridger\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12\x16\n\x0eoracle_address\x18\x02 \x01(\t\x12\x17\n\x0f\x62ridger_address\x18\x03 \x01(\t\"\x18\n\x16MsgEditBridgerResponse\"?\n\x11MsgUnbondedOracle\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12\x16\n\x0eoracle_address\x18\x02 \x01(\t\"\x1b\n\x19MsgUnbondedOracleResponse\"?\n\x11MsgWithdrawReward\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12\x16\n\x0eoracle_address\x18\x02 \x01(\t\"\x1b\n\x19MsgWithdrawRewardResponse\"~\n\x13MsgOracleSetConfirm\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x17\n\x0f\x62ridger_address\x18\x02 \x01(\t\x12\x18\n\x10\x65xternal_address\x18\x03 \x01(\t\x12\x11\n\tsignature\x18\x04 \x01(\t\x12\x12\n\nchain_name\x18\x05 \x01(\t\"\x1d\n\x1bMsgOracleSetConfirmResponse\"\xce\x01\n\x18MsgOracleSetUpdatedClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x04\x12\x18\n\x10oracle_set_nonce\x18\x03 \x01(\x04\x12@\n\x07members\x18\x04 \x03(\x0b\x32).fx.gravity.crosschain.v1.BridgeValidatorB\x04\xc8\xde\x1f\x00\x12\x17\n\x0f\x62ridger_address\x18\x06 \x01(\t\x12\x12\n\nchain_name\x18\x07 \x01(\t\"\"\n MsgOracleSetUpdatedClaimResponse\"\xf8\x01\n\x10MsgSendToFxClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x04\x12\x16\n\x0etoken_contract\x18\x03 \x01(\t\x12>\n\x06\x61mount\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x0e\n\x06sender\x18\x05 \x01(\t\x12\x10\n\x08receiver\x18\x06 \x01(\t\x12\x12\n\ntarget_ibc\x18\x07 \x01(\t\x12\x17\n\x0f\x62ridger_address\x18\x08 \x01(\t\x12\x12\n\nchain_name\x18\t \x01(\t\"\x1a\n\x18MsgSendToFxClaimResponse\"\xab\x01\n\x11MsgSendToExternal\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65st\x18\x02 \x01(\t\x12/\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x33\n\nbridge_fee\x18\x04 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x12\n\nchain_name\x18\x05 \x01(\t\"3\n\x19MsgSendToExternalResponse\x12\x16\n\x0eoutgoing_tx_id\x18\x01 \x01(\x04\"U\n\x17MsgCancelSendToExternal\x12\x16\n\x0etransaction_id\x18\x01 \x01(\x04\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12\x12\n\nchain_name\x18\x03 \x01(\t\"!\n\x1fMsgCancelSendToExternalResponse\"\xe0\x01\n\x0fMsgRequestBatch\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t\x12\x43\n\x0bminimum_fee\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x13\n\x0b\x66\x65\x65_receive\x18\x04 \x01(\t\x12\x12\n\nchain_name\x18\x05 \x01(\t\x12@\n\x08\x62\x61se_fee\x18\x06 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\".\n\x17MsgRequestBatchResponse\x12\x13\n\x0b\x62\x61tch_nonce\x18\x01 \x01(\x04\"\x92\x01\n\x0fMsgConfirmBatch\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x16\n\x0etoken_contract\x18\x02 \x01(\t\x12\x17\n\x0f\x62ridger_address\x18\x03 \x01(\t\x12\x18\n\x10\x65xternal_address\x18\x04 \x01(\t\x12\x11\n\tsignature\x18\x05 \x01(\t\x12\x12\n\nchain_name\x18\x06 \x01(\t\"\x19\n\x17MsgConfirmBatchResponse\"\x9d\x01\n\x16MsgSendToExternalClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x04\x12\x13\n\x0b\x62\x61tch_nonce\x18\x03 \x01(\x04\x12\x16\n\x0etoken_contract\x18\x04 \x01(\t\x12\x17\n\x0f\x62ridger_address\x18\x05 \x01(\t\x12\x12\n\nchain_name\x18\x06 \x01(\t\" \n\x1eMsgSendToExternalClaimResponse\"\xca\x01\n\x13MsgBridgeTokenClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x04\x12\x16\n\x0etoken_contract\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0e\n\x06symbol\x18\x05 \x01(\t\x12\x10\n\x08\x64\x65\x63imals\x18\x06 \x01(\x04\x12\x17\n\x0f\x62ridger_address\x18\x07 \x01(\t\x12\x13\n\x0b\x63hannel_ibc\x18\x08 \x01(\t\x12\x12\n\nchain_name\x18\t \x01(\t\"\x1d\n\x1bMsgBridgeTokenClaimResponse\"\xac\x01\n\x19MsgSetOrchestratorAddress\x12\x16\n\x0eoracle_address\x18\x01 \x01(\t\x12\x17\n\x0f\x62ridger_address\x18\x02 \x01(\t\x12\x18\n\x10\x65xternal_address\x18\x03 \x01(\t\x12\x30\n\x07\x64\x65posit\x18\x04 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x12\n\nchain_name\x18\x05 \x01(\t\"r\n\x13MsgAddOracleDeposit\x12\x16\n\x0eoracle_address\x18\x01 \x01(\t\x12/\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x12\n\nchain_name\x18\x03 \x01(\t\"\x9a\x01\n\x0fMsgUpdateParams\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12+\n\tauthority\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x36\n\x06params\x18\x03 \x01(\x0b\x32 .fx.gravity.crosschain.v1.ParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x19\n\x17MsgUpdateParamsResponse\"\x8b\x01\n\x14MsgIncreaseBridgeFee\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12\x16\n\x0etransaction_id\x18\x02 \x01(\x04\x12\x0e\n\x06sender\x18\x03 \x01(\t\x12\x37\n\x0e\x61\x64\x64_bridge_fee\x18\x04 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\x1e\n\x1cMsgIncreaseBridgeFeeResponse\"y\n\x15MsgUpdateChainOracles\x12\x12\n\nchain_name\x18\x01 \x01(\t\x12+\n\tauthority\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x0f\n\x07oracles\x18\x03 \x03(\t:\x0e\x82\xe7\xb0*\tauthority\"\x1f\n\x1dMsgUpdateChainOraclesResponse2\xcd\x10\n\x03Msg\x12l\n\x0c\x42ondedOracle\x12).fx.gravity.crosschain.v1.MsgBondedOracle\x1a\x31.fx.gravity.crosschain.v1.MsgBondedOracleResponse\x12i\n\x0b\x41\x64\x64\x44\x65legate\x12(.fx.gravity.crosschain.v1.MsgAddDelegate\x1a\x30.fx.gravity.crosschain.v1.MsgAddDelegateResponse\x12\x66\n\nReDelegate\x12\'.fx.gravity.crosschain.v1.MsgReDelegate\x1a/.fx.gravity.crosschain.v1.MsgReDelegateResponse\x12i\n\x0b\x45\x64itBridger\x12(.fx.gravity.crosschain.v1.MsgEditBridger\x1a\x30.fx.gravity.crosschain.v1.MsgEditBridgerResponse\x12r\n\x0eWithdrawReward\x12+.fx.gravity.crosschain.v1.MsgWithdrawReward\x1a\x33.fx.gravity.crosschain.v1.MsgWithdrawRewardResponse\x12r\n\x0eUnbondedOracle\x12+.fx.gravity.crosschain.v1.MsgUnbondedOracle\x1a\x33.fx.gravity.crosschain.v1.MsgUnbondedOracleResponse\x12x\n\x10OracleSetConfirm\x12-.fx.gravity.crosschain.v1.MsgOracleSetConfirm\x1a\x35.fx.gravity.crosschain.v1.MsgOracleSetConfirmResponse\x12\x86\x01\n\x14OracleSetUpdateClaim\x12\x32.fx.gravity.crosschain.v1.MsgOracleSetUpdatedClaim\x1a:.fx.gravity.crosschain.v1.MsgOracleSetUpdatedClaimResponse\x12x\n\x10\x42ridgeTokenClaim\x12-.fx.gravity.crosschain.v1.MsgBridgeTokenClaim\x1a\x35.fx.gravity.crosschain.v1.MsgBridgeTokenClaimResponse\x12o\n\rSendToFxClaim\x12*.fx.gravity.crosschain.v1.MsgSendToFxClaim\x1a\x32.fx.gravity.crosschain.v1.MsgSendToFxClaimResponse\x12r\n\x0eSendToExternal\x12+.fx.gravity.crosschain.v1.MsgSendToExternal\x1a\x33.fx.gravity.crosschain.v1.MsgSendToExternalResponse\x12\x84\x01\n\x14\x43\x61ncelSendToExternal\x12\x31.fx.gravity.crosschain.v1.MsgCancelSendToExternal\x1a\x39.fx.gravity.crosschain.v1.MsgCancelSendToExternalResponse\x12\x81\x01\n\x13SendToExternalClaim\x12\x30.fx.gravity.crosschain.v1.MsgSendToExternalClaim\x1a\x38.fx.gravity.crosschain.v1.MsgSendToExternalClaimResponse\x12l\n\x0cRequestBatch\x12).fx.gravity.crosschain.v1.MsgRequestBatch\x1a\x31.fx.gravity.crosschain.v1.MsgRequestBatchResponse\x12l\n\x0c\x43onfirmBatch\x12).fx.gravity.crosschain.v1.MsgConfirmBatch\x1a\x31.fx.gravity.crosschain.v1.MsgConfirmBatchResponse\x12l\n\x0cUpdateParams\x12).fx.gravity.crosschain.v1.MsgUpdateParams\x1a\x31.fx.gravity.crosschain.v1.MsgUpdateParamsResponse\x12{\n\x11IncreaseBridgeFee\x12..fx.gravity.crosschain.v1.MsgIncreaseBridgeFee\x1a\x36.fx.gravity.crosschain.v1.MsgIncreaseBridgeFeeResponse\x12~\n\x12UpdateChainOracles\x12/.fx.gravity.crosschain.v1.MsgUpdateChainOracles\x1a\x37.fx.gravity.crosschain.v1.MsgUpdateChainOraclesResponseB1Z/github.com/functionx/fx-core/x/crosschain/typesb\x06proto3')



_MSGBONDEDORACLE = DESCRIPTOR.message_types_by_name['MsgBondedOracle']
_MSGBONDEDORACLERESPONSE = DESCRIPTOR.message_types_by_name['MsgBondedOracleResponse']
_MSGADDDELEGATE = DESCRIPTOR.message_types_by_name['MsgAddDelegate']
_MSGADDDELEGATERESPONSE = DESCRIPTOR.message_types_by_name['MsgAddDelegateResponse']
_MSGREDELEGATE = DESCRIPTOR.message_types_by_name['MsgReDelegate']
_MSGREDELEGATERESPONSE = DESCRIPTOR.message_types_by_name['MsgReDelegateResponse']
_MSGEDITBRIDGER = DESCRIPTOR.message_types_by_name['MsgEditBridger']
_MSGEDITBRIDGERRESPONSE = DESCRIPTOR.message_types_by_name['MsgEditBridgerResponse']
_MSGUNBONDEDORACLE = DESCRIPTOR.message_types_by_name['MsgUnbondedOracle']
_MSGUNBONDEDORACLERESPONSE = DESCRIPTOR.message_types_by_name['MsgUnbondedOracleResponse']
_MSGWITHDRAWREWARD = DESCRIPTOR.message_types_by_name['MsgWithdrawReward']
_MSGWITHDRAWREWARDRESPONSE = DESCRIPTOR.message_types_by_name['MsgWithdrawRewardResponse']
_MSGORACLESETCONFIRM = DESCRIPTOR.message_types_by_name['MsgOracleSetConfirm']
_MSGORACLESETCONFIRMRESPONSE = DESCRIPTOR.message_types_by_name['MsgOracleSetConfirmResponse']
_MSGORACLESETUPDATEDCLAIM = DESCRIPTOR.message_types_by_name['MsgOracleSetUpdatedClaim']
_MSGORACLESETUPDATEDCLAIMRESPONSE = DESCRIPTOR.message_types_by_name['MsgOracleSetUpdatedClaimResponse']
_MSGSENDTOFXCLAIM = DESCRIPTOR.message_types_by_name['MsgSendToFxClaim']
_MSGSENDTOFXCLAIMRESPONSE = DESCRIPTOR.message_types_by_name['MsgSendToFxClaimResponse']
_MSGSENDTOEXTERNAL = DESCRIPTOR.message_types_by_name['MsgSendToExternal']
_MSGSENDTOEXTERNALRESPONSE = DESCRIPTOR.message_types_by_name['MsgSendToExternalResponse']
_MSGCANCELSENDTOEXTERNAL = DESCRIPTOR.message_types_by_name['MsgCancelSendToExternal']
_MSGCANCELSENDTOEXTERNALRESPONSE = DESCRIPTOR.message_types_by_name['MsgCancelSendToExternalResponse']
_MSGREQUESTBATCH = DESCRIPTOR.message_types_by_name['MsgRequestBatch']
_MSGREQUESTBATCHRESPONSE = DESCRIPTOR.message_types_by_name['MsgRequestBatchResponse']
_MSGCONFIRMBATCH = DESCRIPTOR.message_types_by_name['MsgConfirmBatch']
_MSGCONFIRMBATCHRESPONSE = DESCRIPTOR.message_types_by_name['MsgConfirmBatchResponse']
_MSGSENDTOEXTERNALCLAIM = DESCRIPTOR.message_types_by_name['MsgSendToExternalClaim']
_MSGSENDTOEXTERNALCLAIMRESPONSE = DESCRIPTOR.message_types_by_name['MsgSendToExternalClaimResponse']
_MSGBRIDGETOKENCLAIM = DESCRIPTOR.message_types_by_name['MsgBridgeTokenClaim']
_MSGBRIDGETOKENCLAIMRESPONSE = DESCRIPTOR.message_types_by_name['MsgBridgeTokenClaimResponse']
_MSGSETORCHESTRATORADDRESS = DESCRIPTOR.message_types_by_name['MsgSetOrchestratorAddress']
_MSGADDORACLEDEPOSIT = DESCRIPTOR.message_types_by_name['MsgAddOracleDeposit']
_MSGUPDATEPARAMS = DESCRIPTOR.message_types_by_name['MsgUpdateParams']
_MSGUPDATEPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['MsgUpdateParamsResponse']
_MSGINCREASEBRIDGEFEE = DESCRIPTOR.message_types_by_name['MsgIncreaseBridgeFee']
_MSGINCREASEBRIDGEFEERESPONSE = DESCRIPTOR.message_types_by_name['MsgIncreaseBridgeFeeResponse']
_MSGUPDATECHAINORACLES = DESCRIPTOR.message_types_by_name['MsgUpdateChainOracles']
_MSGUPDATECHAINORACLESRESPONSE = DESCRIPTOR.message_types_by_name['MsgUpdateChainOraclesResponse']
MsgBondedOracle = _reflection.GeneratedProtocolMessageType('MsgBondedOracle', (_message.Message,), {
  'DESCRIPTOR' : _MSGBONDEDORACLE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgBondedOracle)
  })
_sym_db.RegisterMessage(MsgBondedOracle)

MsgBondedOracleResponse = _reflection.GeneratedProtocolMessageType('MsgBondedOracleResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGBONDEDORACLERESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgBondedOracleResponse)
  })
_sym_db.RegisterMessage(MsgBondedOracleResponse)

MsgAddDelegate = _reflection.GeneratedProtocolMessageType('MsgAddDelegate', (_message.Message,), {
  'DESCRIPTOR' : _MSGADDDELEGATE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgAddDelegate)
  })
_sym_db.RegisterMessage(MsgAddDelegate)

MsgAddDelegateResponse = _reflection.GeneratedProtocolMessageType('MsgAddDelegateResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGADDDELEGATERESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgAddDelegateResponse)
  })
_sym_db.RegisterMessage(MsgAddDelegateResponse)

MsgReDelegate = _reflection.GeneratedProtocolMessageType('MsgReDelegate', (_message.Message,), {
  'DESCRIPTOR' : _MSGREDELEGATE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgReDelegate)
  })
_sym_db.RegisterMessage(MsgReDelegate)

MsgReDelegateResponse = _reflection.GeneratedProtocolMessageType('MsgReDelegateResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGREDELEGATERESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgReDelegateResponse)
  })
_sym_db.RegisterMessage(MsgReDelegateResponse)

MsgEditBridger = _reflection.GeneratedProtocolMessageType('MsgEditBridger', (_message.Message,), {
  'DESCRIPTOR' : _MSGEDITBRIDGER,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgEditBridger)
  })
_sym_db.RegisterMessage(MsgEditBridger)

MsgEditBridgerResponse = _reflection.GeneratedProtocolMessageType('MsgEditBridgerResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGEDITBRIDGERRESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgEditBridgerResponse)
  })
_sym_db.RegisterMessage(MsgEditBridgerResponse)

MsgUnbondedOracle = _reflection.GeneratedProtocolMessageType('MsgUnbondedOracle', (_message.Message,), {
  'DESCRIPTOR' : _MSGUNBONDEDORACLE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgUnbondedOracle)
  })
_sym_db.RegisterMessage(MsgUnbondedOracle)

MsgUnbondedOracleResponse = _reflection.GeneratedProtocolMessageType('MsgUnbondedOracleResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGUNBONDEDORACLERESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgUnbondedOracleResponse)
  })
_sym_db.RegisterMessage(MsgUnbondedOracleResponse)

MsgWithdrawReward = _reflection.GeneratedProtocolMessageType('MsgWithdrawReward', (_message.Message,), {
  'DESCRIPTOR' : _MSGWITHDRAWREWARD,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgWithdrawReward)
  })
_sym_db.RegisterMessage(MsgWithdrawReward)

MsgWithdrawRewardResponse = _reflection.GeneratedProtocolMessageType('MsgWithdrawRewardResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGWITHDRAWREWARDRESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgWithdrawRewardResponse)
  })
_sym_db.RegisterMessage(MsgWithdrawRewardResponse)

MsgOracleSetConfirm = _reflection.GeneratedProtocolMessageType('MsgOracleSetConfirm', (_message.Message,), {
  'DESCRIPTOR' : _MSGORACLESETCONFIRM,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgOracleSetConfirm)
  })
_sym_db.RegisterMessage(MsgOracleSetConfirm)

MsgOracleSetConfirmResponse = _reflection.GeneratedProtocolMessageType('MsgOracleSetConfirmResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGORACLESETCONFIRMRESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgOracleSetConfirmResponse)
  })
_sym_db.RegisterMessage(MsgOracleSetConfirmResponse)

MsgOracleSetUpdatedClaim = _reflection.GeneratedProtocolMessageType('MsgOracleSetUpdatedClaim', (_message.Message,), {
  'DESCRIPTOR' : _MSGORACLESETUPDATEDCLAIM,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgOracleSetUpdatedClaim)
  })
_sym_db.RegisterMessage(MsgOracleSetUpdatedClaim)

MsgOracleSetUpdatedClaimResponse = _reflection.GeneratedProtocolMessageType('MsgOracleSetUpdatedClaimResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGORACLESETUPDATEDCLAIMRESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgOracleSetUpdatedClaimResponse)
  })
_sym_db.RegisterMessage(MsgOracleSetUpdatedClaimResponse)

MsgSendToFxClaim = _reflection.GeneratedProtocolMessageType('MsgSendToFxClaim', (_message.Message,), {
  'DESCRIPTOR' : _MSGSENDTOFXCLAIM,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgSendToFxClaim)
  })
_sym_db.RegisterMessage(MsgSendToFxClaim)

MsgSendToFxClaimResponse = _reflection.GeneratedProtocolMessageType('MsgSendToFxClaimResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGSENDTOFXCLAIMRESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgSendToFxClaimResponse)
  })
_sym_db.RegisterMessage(MsgSendToFxClaimResponse)

MsgSendToExternal = _reflection.GeneratedProtocolMessageType('MsgSendToExternal', (_message.Message,), {
  'DESCRIPTOR' : _MSGSENDTOEXTERNAL,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgSendToExternal)
  })
_sym_db.RegisterMessage(MsgSendToExternal)

MsgSendToExternalResponse = _reflection.GeneratedProtocolMessageType('MsgSendToExternalResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGSENDTOEXTERNALRESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgSendToExternalResponse)
  })
_sym_db.RegisterMessage(MsgSendToExternalResponse)

MsgCancelSendToExternal = _reflection.GeneratedProtocolMessageType('MsgCancelSendToExternal', (_message.Message,), {
  'DESCRIPTOR' : _MSGCANCELSENDTOEXTERNAL,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgCancelSendToExternal)
  })
_sym_db.RegisterMessage(MsgCancelSendToExternal)

MsgCancelSendToExternalResponse = _reflection.GeneratedProtocolMessageType('MsgCancelSendToExternalResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCANCELSENDTOEXTERNALRESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgCancelSendToExternalResponse)
  })
_sym_db.RegisterMessage(MsgCancelSendToExternalResponse)

MsgRequestBatch = _reflection.GeneratedProtocolMessageType('MsgRequestBatch', (_message.Message,), {
  'DESCRIPTOR' : _MSGREQUESTBATCH,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgRequestBatch)
  })
_sym_db.RegisterMessage(MsgRequestBatch)

MsgRequestBatchResponse = _reflection.GeneratedProtocolMessageType('MsgRequestBatchResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGREQUESTBATCHRESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgRequestBatchResponse)
  })
_sym_db.RegisterMessage(MsgRequestBatchResponse)

MsgConfirmBatch = _reflection.GeneratedProtocolMessageType('MsgConfirmBatch', (_message.Message,), {
  'DESCRIPTOR' : _MSGCONFIRMBATCH,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgConfirmBatch)
  })
_sym_db.RegisterMessage(MsgConfirmBatch)

MsgConfirmBatchResponse = _reflection.GeneratedProtocolMessageType('MsgConfirmBatchResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCONFIRMBATCHRESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgConfirmBatchResponse)
  })
_sym_db.RegisterMessage(MsgConfirmBatchResponse)

MsgSendToExternalClaim = _reflection.GeneratedProtocolMessageType('MsgSendToExternalClaim', (_message.Message,), {
  'DESCRIPTOR' : _MSGSENDTOEXTERNALCLAIM,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgSendToExternalClaim)
  })
_sym_db.RegisterMessage(MsgSendToExternalClaim)

MsgSendToExternalClaimResponse = _reflection.GeneratedProtocolMessageType('MsgSendToExternalClaimResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGSENDTOEXTERNALCLAIMRESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgSendToExternalClaimResponse)
  })
_sym_db.RegisterMessage(MsgSendToExternalClaimResponse)

MsgBridgeTokenClaim = _reflection.GeneratedProtocolMessageType('MsgBridgeTokenClaim', (_message.Message,), {
  'DESCRIPTOR' : _MSGBRIDGETOKENCLAIM,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgBridgeTokenClaim)
  })
_sym_db.RegisterMessage(MsgBridgeTokenClaim)

MsgBridgeTokenClaimResponse = _reflection.GeneratedProtocolMessageType('MsgBridgeTokenClaimResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGBRIDGETOKENCLAIMRESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgBridgeTokenClaimResponse)
  })
_sym_db.RegisterMessage(MsgBridgeTokenClaimResponse)

MsgSetOrchestratorAddress = _reflection.GeneratedProtocolMessageType('MsgSetOrchestratorAddress', (_message.Message,), {
  'DESCRIPTOR' : _MSGSETORCHESTRATORADDRESS,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgSetOrchestratorAddress)
  })
_sym_db.RegisterMessage(MsgSetOrchestratorAddress)

MsgAddOracleDeposit = _reflection.GeneratedProtocolMessageType('MsgAddOracleDeposit', (_message.Message,), {
  'DESCRIPTOR' : _MSGADDORACLEDEPOSIT,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgAddOracleDeposit)
  })
_sym_db.RegisterMessage(MsgAddOracleDeposit)

MsgUpdateParams = _reflection.GeneratedProtocolMessageType('MsgUpdateParams', (_message.Message,), {
  'DESCRIPTOR' : _MSGUPDATEPARAMS,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgUpdateParams)
  })
_sym_db.RegisterMessage(MsgUpdateParams)

MsgUpdateParamsResponse = _reflection.GeneratedProtocolMessageType('MsgUpdateParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGUPDATEPARAMSRESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgUpdateParamsResponse)
  })
_sym_db.RegisterMessage(MsgUpdateParamsResponse)

MsgIncreaseBridgeFee = _reflection.GeneratedProtocolMessageType('MsgIncreaseBridgeFee', (_message.Message,), {
  'DESCRIPTOR' : _MSGINCREASEBRIDGEFEE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgIncreaseBridgeFee)
  })
_sym_db.RegisterMessage(MsgIncreaseBridgeFee)

MsgIncreaseBridgeFeeResponse = _reflection.GeneratedProtocolMessageType('MsgIncreaseBridgeFeeResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGINCREASEBRIDGEFEERESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgIncreaseBridgeFeeResponse)
  })
_sym_db.RegisterMessage(MsgIncreaseBridgeFeeResponse)

MsgUpdateChainOracles = _reflection.GeneratedProtocolMessageType('MsgUpdateChainOracles', (_message.Message,), {
  'DESCRIPTOR' : _MSGUPDATECHAINORACLES,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgUpdateChainOracles)
  })
_sym_db.RegisterMessage(MsgUpdateChainOracles)

MsgUpdateChainOraclesResponse = _reflection.GeneratedProtocolMessageType('MsgUpdateChainOraclesResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGUPDATECHAINORACLESRESPONSE,
  '__module__' : 'fx.crosschain.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.gravity.crosschain.v1.MsgUpdateChainOraclesResponse)
  })
_sym_db.RegisterMessage(MsgUpdateChainOraclesResponse)

_MSG = DESCRIPTOR.services_by_name['Msg']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/github.com/functionx/fx-core/x/crosschain/types'
  _MSGBONDEDORACLE.fields_by_name['delegate_amount']._options = None
  _MSGBONDEDORACLE.fields_by_name['delegate_amount']._serialized_options = b'\310\336\037\000'
  _MSGADDDELEGATE.fields_by_name['amount']._options = None
  _MSGADDDELEGATE.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _MSGORACLESETUPDATEDCLAIM.fields_by_name['members']._options = None
  _MSGORACLESETUPDATEDCLAIM.fields_by_name['members']._serialized_options = b'\310\336\037\000'
  _MSGSENDTOFXCLAIM.fields_by_name['amount']._options = None
  _MSGSENDTOFXCLAIM.fields_by_name['amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _MSGSENDTOEXTERNAL.fields_by_name['amount']._options = None
  _MSGSENDTOEXTERNAL.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _MSGSENDTOEXTERNAL.fields_by_name['bridge_fee']._options = None
  _MSGSENDTOEXTERNAL.fields_by_name['bridge_fee']._serialized_options = b'\310\336\037\000'
  _MSGREQUESTBATCH.fields_by_name['minimum_fee']._options = None
  _MSGREQUESTBATCH.fields_by_name['minimum_fee']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _MSGREQUESTBATCH.fields_by_name['base_fee']._options = None
  _MSGREQUESTBATCH.fields_by_name['base_fee']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _MSGSETORCHESTRATORADDRESS.fields_by_name['deposit']._options = None
  _MSGSETORCHESTRATORADDRESS.fields_by_name['deposit']._serialized_options = b'\310\336\037\000'
  _MSGADDORACLEDEPOSIT.fields_by_name['amount']._options = None
  _MSGADDORACLEDEPOSIT.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEPARAMS.fields_by_name['authority']._options = None
  _MSGUPDATEPARAMS.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEPARAMS.fields_by_name['params']._options = None
  _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEPARAMS._options = None
  _MSGUPDATEPARAMS._serialized_options = b'\202\347\260*\tauthority'
  _MSGINCREASEBRIDGEFEE.fields_by_name['add_bridge_fee']._options = None
  _MSGINCREASEBRIDGEFEE.fields_by_name['add_bridge_fee']._serialized_options = b'\310\336\037\000'
  _MSGUPDATECHAINORACLES.fields_by_name['authority']._options = None
  _MSGUPDATECHAINORACLES.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATECHAINORACLES._options = None
  _MSGUPDATECHAINORACLES._serialized_options = b'\202\347\260*\tauthority'
  _MSGBONDEDORACLE._serialized_start=192
  _MSGBONDEDORACLE._serialized_end=389
  _MSGBONDEDORACLERESPONSE._serialized_start=391
  _MSGBONDEDORACLERESPONSE._serialized_end=416
  _MSGADDDELEGATE._serialized_start=418
  _MSGADDDELEGATE._serialized_end=527
  _MSGADDDELEGATERESPONSE._serialized_start=529
  _MSGADDDELEGATERESPONSE._serialized_end=553
  _MSGREDELEGATE._serialized_start=555
  _MSGREDELEGATE._serialized_end=641
  _MSGREDELEGATERESPONSE._serialized_start=643
  _MSGREDELEGATERESPONSE._serialized_end=666
  _MSGEDITBRIDGER._serialized_start=668
  _MSGEDITBRIDGER._serialized_end=753
  _MSGEDITBRIDGERRESPONSE._serialized_start=755
  _MSGEDITBRIDGERRESPONSE._serialized_end=779
  _MSGUNBONDEDORACLE._serialized_start=781
  _MSGUNBONDEDORACLE._serialized_end=844
  _MSGUNBONDEDORACLERESPONSE._serialized_start=846
  _MSGUNBONDEDORACLERESPONSE._serialized_end=873
  _MSGWITHDRAWREWARD._serialized_start=875
  _MSGWITHDRAWREWARD._serialized_end=938
  _MSGWITHDRAWREWARDRESPONSE._serialized_start=940
  _MSGWITHDRAWREWARDRESPONSE._serialized_end=967
  _MSGORACLESETCONFIRM._serialized_start=969
  _MSGORACLESETCONFIRM._serialized_end=1095
  _MSGORACLESETCONFIRMRESPONSE._serialized_start=1097
  _MSGORACLESETCONFIRMRESPONSE._serialized_end=1126
  _MSGORACLESETUPDATEDCLAIM._serialized_start=1129
  _MSGORACLESETUPDATEDCLAIM._serialized_end=1335
  _MSGORACLESETUPDATEDCLAIMRESPONSE._serialized_start=1337
  _MSGORACLESETUPDATEDCLAIMRESPONSE._serialized_end=1371
  _MSGSENDTOFXCLAIM._serialized_start=1374
  _MSGSENDTOFXCLAIM._serialized_end=1622
  _MSGSENDTOFXCLAIMRESPONSE._serialized_start=1624
  _MSGSENDTOFXCLAIMRESPONSE._serialized_end=1650
  _MSGSENDTOEXTERNAL._serialized_start=1653
  _MSGSENDTOEXTERNAL._serialized_end=1824
  _MSGSENDTOEXTERNALRESPONSE._serialized_start=1826
  _MSGSENDTOEXTERNALRESPONSE._serialized_end=1877
  _MSGCANCELSENDTOEXTERNAL._serialized_start=1879
  _MSGCANCELSENDTOEXTERNAL._serialized_end=1964
  _MSGCANCELSENDTOEXTERNALRESPONSE._serialized_start=1966
  _MSGCANCELSENDTOEXTERNALRESPONSE._serialized_end=1999
  _MSGREQUESTBATCH._serialized_start=2002
  _MSGREQUESTBATCH._serialized_end=2226
  _MSGREQUESTBATCHRESPONSE._serialized_start=2228
  _MSGREQUESTBATCHRESPONSE._serialized_end=2274
  _MSGCONFIRMBATCH._serialized_start=2277
  _MSGCONFIRMBATCH._serialized_end=2423
  _MSGCONFIRMBATCHRESPONSE._serialized_start=2425
  _MSGCONFIRMBATCHRESPONSE._serialized_end=2450
  _MSGSENDTOEXTERNALCLAIM._serialized_start=2453
  _MSGSENDTOEXTERNALCLAIM._serialized_end=2610
  _MSGSENDTOEXTERNALCLAIMRESPONSE._serialized_start=2612
  _MSGSENDTOEXTERNALCLAIMRESPONSE._serialized_end=2644
  _MSGBRIDGETOKENCLAIM._serialized_start=2647
  _MSGBRIDGETOKENCLAIM._serialized_end=2849
  _MSGBRIDGETOKENCLAIMRESPONSE._serialized_start=2851
  _MSGBRIDGETOKENCLAIMRESPONSE._serialized_end=2880
  _MSGSETORCHESTRATORADDRESS._serialized_start=2883
  _MSGSETORCHESTRATORADDRESS._serialized_end=3055
  _MSGADDORACLEDEPOSIT._serialized_start=3057
  _MSGADDORACLEDEPOSIT._serialized_end=3171
  _MSGUPDATEPARAMS._serialized_start=3174
  _MSGUPDATEPARAMS._serialized_end=3328
  _MSGUPDATEPARAMSRESPONSE._serialized_start=3330
  _MSGUPDATEPARAMSRESPONSE._serialized_end=3355
  _MSGINCREASEBRIDGEFEE._serialized_start=3358
  _MSGINCREASEBRIDGEFEE._serialized_end=3497
  _MSGINCREASEBRIDGEFEERESPONSE._serialized_start=3499
  _MSGINCREASEBRIDGEFEERESPONSE._serialized_end=3529
  _MSGUPDATECHAINORACLES._serialized_start=3531
  _MSGUPDATECHAINORACLES._serialized_end=3652
  _MSGUPDATECHAINORACLESRESPONSE._serialized_start=3654
  _MSGUPDATECHAINORACLESRESPONSE._serialized_end=3685
  _MSG._serialized_start=3688
  _MSG._serialized_end=5813
# @@protoc_insertion_point(module_scope)