# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: marginx/oracle/v1/types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from fxsdk.x.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dmarginx/oracle/v1/types.proto\x12\x11marginx.oracle.v1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\"$\n\x06Params\x12\x1a\n\x12price_quote_symbol\x18\x01 \x01(\t\"\xbf\x01\n\x06Market\x12\x0f\n\x07pair_id\x18\x01 \x01(\t\x12\x12\n\nbase_asset\x18\x02 \x01(\t\x12\x13\n\x0bquote_asset\x18\x03 \x01(\t\x12\x36\n\rmarket_status\x18\x05 \x01(\x0e\x32\x1f.marginx.oracle.v1.MarketStatus\x12\x15\n\rprice_decimal\x18\x06 \x01(\x03\x12\x18\n\x10position_decimal\x18\x07 \x01(\x03\x12\x12\n\x04type\x18\x08 \x01(\tB\x04\xc8\xde\x1f\x01\"[\n\x06\x41nswer\x12\x0e\n\x06oracle\x18\x01 \x01(\t\x12\x41\n\x06\x61nswer\x18\x02 \x01(\tB1\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\"Y\n\x05Price\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\tB1\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\"\xb7\x01\n\nAggregator\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x35\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x1f.marginx.oracle.v1.OracleConfigB\x04\xc8\xde\x1f\x00\x12\x18\n\x10round_start_time\x18\x03 \x01(\x03\x12\x34\n\x0bsubmissions\x18\x04 \x03(\x0b\x32\x19.marginx.oracle.v1.AnswerB\x04\xc8\xde\x1f\x00\x12\x12\n\x04type\x18\x05 \x01(\tB\x04\xc8\xde\x1f\x01\"Z\n\x0cOracleConfig\x12\x0f\n\x07oracles\x18\x01 \x03(\t\x12\x1c\n\x14min_answer_threshold\x18\x02 \x01(\r\x12\x1b\n\x13staleness_threshold\x18\x03 \x01(\x03*\xe6\x01\n\x0cMarketStatus\x12\x34\n\x19MARKET_STATUS_UNSPECIFIED\x10\x00\x1a\x15\x8a\x9d \x11MarketStatusEmpty\x12\x30\n\x14MARKET_STATUS_LISTED\x10\x01\x1a\x16\x8a\x9d \x12MarketStatusListed\x12\x32\n\x15MARKET_STATUS_SUSPEND\x10\x02\x1a\x17\x8a\x9d \x13MarketStatusSuspend\x12\x30\n\x14MARKET_STATUS_PRESET\x10\x03\x1a\x16\x8a\x9d \x12MarketStatusPreset\x1a\x08\x88\xa3\x1e\x00\xa8\xa4\x1e\x01\x42-Z+github.com/marginxio/marginx/x/oracle/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'marginx.oracle.v1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/marginxio/marginx/x/oracle/types'
  _MARKETSTATUS._options = None
  _MARKETSTATUS._serialized_options = b'\210\243\036\000\250\244\036\001'
  _MARKETSTATUS.values_by_name["MARKET_STATUS_UNSPECIFIED"]._options = None
  _MARKETSTATUS.values_by_name["MARKET_STATUS_UNSPECIFIED"]._serialized_options = b'\212\235 \021MarketStatusEmpty'
  _MARKETSTATUS.values_by_name["MARKET_STATUS_LISTED"]._options = None
  _MARKETSTATUS.values_by_name["MARKET_STATUS_LISTED"]._serialized_options = b'\212\235 \022MarketStatusListed'
  _MARKETSTATUS.values_by_name["MARKET_STATUS_SUSPEND"]._options = None
  _MARKETSTATUS.values_by_name["MARKET_STATUS_SUSPEND"]._serialized_options = b'\212\235 \023MarketStatusSuspend'
  _MARKETSTATUS.values_by_name["MARKET_STATUS_PRESET"]._options = None
  _MARKETSTATUS.values_by_name["MARKET_STATUS_PRESET"]._serialized_options = b'\212\235 \022MarketStatusPreset'
  _MARKET.fields_by_name['type']._options = None
  _MARKET.fields_by_name['type']._serialized_options = b'\310\336\037\001'
  _ANSWER.fields_by_name['answer']._options = None
  _ANSWER.fields_by_name['answer']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec'
  _PRICE.fields_by_name['value']._options = None
  _PRICE.fields_by_name['value']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec'
  _AGGREGATOR.fields_by_name['config']._options = None
  _AGGREGATOR.fields_by_name['config']._serialized_options = b'\310\336\037\000'
  _AGGREGATOR.fields_by_name['submissions']._options = None
  _AGGREGATOR.fields_by_name['submissions']._serialized_options = b'\310\336\037\000'
  _AGGREGATOR.fields_by_name['type']._options = None
  _AGGREGATOR.fields_by_name['type']._serialized_options = b'\310\336\037\001'
  _globals['_MARKETSTATUS']._serialized_start=796
  _globals['_MARKETSTATUS']._serialized_end=1026
  _globals['_PARAMS']._serialized_start=101
  _globals['_PARAMS']._serialized_end=137
  _globals['_MARKET']._serialized_start=140
  _globals['_MARKET']._serialized_end=331
  _globals['_ANSWER']._serialized_start=333
  _globals['_ANSWER']._serialized_end=424
  _globals['_PRICE']._serialized_start=426
  _globals['_PRICE']._serialized_end=515
  _globals['_AGGREGATOR']._serialized_start=518
  _globals['_AGGREGATOR']._serialized_end=701
  _globals['_ORACLECONFIG']._serialized_start=703
  _globals['_ORACLECONFIG']._serialized_end=793
# @@protoc_insertion_point(module_scope)
