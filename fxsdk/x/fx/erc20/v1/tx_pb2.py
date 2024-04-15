# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/erc20/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxsdk.x.cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from fxsdk.x.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from fxsdk.x.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from fxsdk.x.fx.erc20.v1 import erc20_pb2 as fx_dot_erc20_dot_v1_dot_erc20__pb2
from fxsdk.x.fx.erc20.v1 import genesis_pb2 as fx_dot_erc20_dot_v1_dot_genesis__pb2
from fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x66x/erc20/v1/tx.proto\x12\x0b\x66x.erc20.v1\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x66x/erc20/v1/erc20.proto\x1a\x19\x66x/erc20/v1/genesis.proto\x1a\x14gogoproto/gogo.proto\"a\n\x0eMsgConvertCoin\x12-\n\x04\x63oin\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x10\n\x08receiver\x18\x02 \x01(\t\x12\x0e\n\x06sender\x18\x03 \x01(\t\"\x18\n\x16MsgConvertCoinResponse\"\x8d\x01\n\x0fMsgConvertERC20\x12\x18\n\x10\x63ontract_address\x18\x01 \x01(\t\x12>\n\x06\x61mount\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12\x10\n\x08receiver\x18\x03 \x01(\t\x12\x0e\n\x06sender\x18\x04 \x01(\t\"\x19\n\x17MsgConvertERC20Response\"r\n\x0fMsgConvertDenom\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08receiver\x18\x02 \x01(\t\x12-\n\x04\x63oin\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x0e\n\x06target\x18\x04 \x01(\t\"\x19\n\x17MsgConvertDenomResponse\"y\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12)\n\x06params\x18\x02 \x01(\x0b\x32\x13.fx.erc20.v1.ParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x19\n\x17MsgUpdateParamsResponse\"\x85\x01\n\x0fMsgRegisterCoin\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x35\n\x08metadata\x18\x02 \x01(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"E\n\x17MsgRegisterCoinResponse\x12*\n\x04pair\x18\x01 \x01(\x0b\x32\x16.fx.erc20.v1.TokenPairB\x04\xc8\xde\x1f\x00\"v\n\x10MsgRegisterERC20\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x14\n\x0c\x65rc20address\x18\x02 \x01(\t\x12\x0f\n\x07\x61liases\x18\x03 \x03(\t:\x0e\x82\xe7\xb0*\tauthority\"F\n\x18MsgRegisterERC20Response\x12*\n\x04pair\x18\x01 \x01(\x0b\x32\x16.fx.erc20.v1.TokenPairB\x04\xc8\xde\x1f\x00\"f\n\x18MsgToggleTokenConversion\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\r\n\x05token\x18\x02 \x01(\t:\x0e\x82\xe7\xb0*\tauthority\"N\n MsgToggleTokenConversionResponse\x12*\n\x04pair\x18\x01 \x01(\x0b\x32\x16.fx.erc20.v1.TokenPairB\x04\xc8\xde\x1f\x00\"p\n\x13MsgUpdateDenomAlias\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t\x12\r\n\x05\x61lias\x18\x03 \x01(\t:\x0e\x82\xe7\xb0*\tauthority\"\x1d\n\x1bMsgUpdateDenomAliasResponse2\xcc\x05\n\x03Msg\x12O\n\x0b\x43onvertCoin\x12\x1b.fx.erc20.v1.MsgConvertCoin\x1a#.fx.erc20.v1.MsgConvertCoinResponse\x12R\n\x0c\x43onvertERC20\x12\x1c.fx.erc20.v1.MsgConvertERC20\x1a$.fx.erc20.v1.MsgConvertERC20Response\x12R\n\x0c\x43onvertDenom\x12\x1c.fx.erc20.v1.MsgConvertDenom\x1a$.fx.erc20.v1.MsgConvertDenomResponse\x12R\n\x0cUpdateParams\x12\x1c.fx.erc20.v1.MsgUpdateParams\x1a$.fx.erc20.v1.MsgUpdateParamsResponse\x12R\n\x0cRegisterCoin\x12\x1c.fx.erc20.v1.MsgRegisterCoin\x1a$.fx.erc20.v1.MsgRegisterCoinResponse\x12U\n\rRegisterERC20\x12\x1d.fx.erc20.v1.MsgRegisterERC20\x1a%.fx.erc20.v1.MsgRegisterERC20Response\x12m\n\x15ToggleTokenConversion\x12%.fx.erc20.v1.MsgToggleTokenConversion\x1a-.fx.erc20.v1.MsgToggleTokenConversionResponse\x12^\n\x10UpdateDenomAlias\x12 .fx.erc20.v1.MsgUpdateDenomAlias\x1a(.fx.erc20.v1.MsgUpdateDenomAliasResponseB,Z*github.com/functionx/fx-core/x/erc20/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fx.erc20.v1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z*github.com/functionx/fx-core/x/erc20/types'
  _MSGCONVERTCOIN.fields_by_name['coin']._options = None
  _MSGCONVERTCOIN.fields_by_name['coin']._serialized_options = b'\310\336\037\000'
  _MSGCONVERTERC20.fields_by_name['amount']._options = None
  _MSGCONVERTERC20.fields_by_name['amount']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int'
  _MSGCONVERTDENOM.fields_by_name['coin']._options = None
  _MSGCONVERTDENOM.fields_by_name['coin']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEPARAMS.fields_by_name['authority']._options = None
  _MSGUPDATEPARAMS.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEPARAMS.fields_by_name['params']._options = None
  _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEPARAMS._options = None
  _MSGUPDATEPARAMS._serialized_options = b'\202\347\260*\tauthority'
  _MSGREGISTERCOIN.fields_by_name['authority']._options = None
  _MSGREGISTERCOIN.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGREGISTERCOIN.fields_by_name['metadata']._options = None
  _MSGREGISTERCOIN.fields_by_name['metadata']._serialized_options = b'\310\336\037\000'
  _MSGREGISTERCOIN._options = None
  _MSGREGISTERCOIN._serialized_options = b'\202\347\260*\tauthority'
  _MSGREGISTERCOINRESPONSE.fields_by_name['pair']._options = None
  _MSGREGISTERCOINRESPONSE.fields_by_name['pair']._serialized_options = b'\310\336\037\000'
  _MSGREGISTERERC20.fields_by_name['authority']._options = None
  _MSGREGISTERERC20.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGREGISTERERC20._options = None
  _MSGREGISTERERC20._serialized_options = b'\202\347\260*\tauthority'
  _MSGREGISTERERC20RESPONSE.fields_by_name['pair']._options = None
  _MSGREGISTERERC20RESPONSE.fields_by_name['pair']._serialized_options = b'\310\336\037\000'
  _MSGTOGGLETOKENCONVERSION.fields_by_name['authority']._options = None
  _MSGTOGGLETOKENCONVERSION.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGTOGGLETOKENCONVERSION._options = None
  _MSGTOGGLETOKENCONVERSION._serialized_options = b'\202\347\260*\tauthority'
  _MSGTOGGLETOKENCONVERSIONRESPONSE.fields_by_name['pair']._options = None
  _MSGTOGGLETOKENCONVERSIONRESPONSE.fields_by_name['pair']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEDENOMALIAS.fields_by_name['authority']._options = None
  _MSGUPDATEDENOMALIAS.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEDENOMALIAS._options = None
  _MSGUPDATEDENOMALIAS._serialized_options = b'\202\347\260*\tauthority'
  _globals['_MSGCONVERTCOIN']._serialized_start=227
  _globals['_MSGCONVERTCOIN']._serialized_end=324
  _globals['_MSGCONVERTCOINRESPONSE']._serialized_start=326
  _globals['_MSGCONVERTCOINRESPONSE']._serialized_end=350
  _globals['_MSGCONVERTERC20']._serialized_start=353
  _globals['_MSGCONVERTERC20']._serialized_end=494
  _globals['_MSGCONVERTERC20RESPONSE']._serialized_start=496
  _globals['_MSGCONVERTERC20RESPONSE']._serialized_end=521
  _globals['_MSGCONVERTDENOM']._serialized_start=523
  _globals['_MSGCONVERTDENOM']._serialized_end=637
  _globals['_MSGCONVERTDENOMRESPONSE']._serialized_start=639
  _globals['_MSGCONVERTDENOMRESPONSE']._serialized_end=664
  _globals['_MSGUPDATEPARAMS']._serialized_start=666
  _globals['_MSGUPDATEPARAMS']._serialized_end=787
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=789
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=814
  _globals['_MSGREGISTERCOIN']._serialized_start=817
  _globals['_MSGREGISTERCOIN']._serialized_end=950
  _globals['_MSGREGISTERCOINRESPONSE']._serialized_start=952
  _globals['_MSGREGISTERCOINRESPONSE']._serialized_end=1021
  _globals['_MSGREGISTERERC20']._serialized_start=1023
  _globals['_MSGREGISTERERC20']._serialized_end=1141
  _globals['_MSGREGISTERERC20RESPONSE']._serialized_start=1143
  _globals['_MSGREGISTERERC20RESPONSE']._serialized_end=1213
  _globals['_MSGTOGGLETOKENCONVERSION']._serialized_start=1215
  _globals['_MSGTOGGLETOKENCONVERSION']._serialized_end=1317
  _globals['_MSGTOGGLETOKENCONVERSIONRESPONSE']._serialized_start=1319
  _globals['_MSGTOGGLETOKENCONVERSIONRESPONSE']._serialized_end=1397
  _globals['_MSGUPDATEDENOMALIAS']._serialized_start=1399
  _globals['_MSGUPDATEDENOMALIAS']._serialized_end=1511
  _globals['_MSGUPDATEDENOMALIASRESPONSE']._serialized_start=1513
  _globals['_MSGUPDATEDENOMALIASRESPONSE']._serialized_end=1542
  _globals['_MSG']._serialized_start=1545
  _globals['_MSG']._serialized_end=2261
# @@protoc_insertion_point(module_scope)
