# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/fee/v1/ack.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!ibc/applications/fee/v1/ack.proto\x12\x17ibc.applications.fee.v1\x1a\x14gogoproto/gogo.proto\"\xe3\x01\n\x1bIncentivizedAcknowledgement\x12;\n\x13\x61pp_acknowledgement\x18\x01 \x01(\x0c\x42\x1e\xf2\xde\x1f\x1ayaml:\"app_acknowledgement\"\x12\x43\n\x17\x66orward_relayer_address\x18\x02 \x01(\tB\"\xf2\xde\x1f\x1eyaml:\"forward_relayer_address\"\x12\x42\n\x16underlying_app_success\x18\x03 \x01(\x08\x42\"\xf2\xde\x1f\x1eyaml:\"underlying_app_successl\"B7Z5github.com/cosmos/ibc-go/v6/modules/apps/29-fee/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.fee.v1.ack_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z5github.com/cosmos/ibc-go/v6/modules/apps/29-fee/types'
  _INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['app_acknowledgement']._options = None
  _INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['app_acknowledgement']._serialized_options = b'\362\336\037\032yaml:\"app_acknowledgement\"'
  _INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['forward_relayer_address']._options = None
  _INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['forward_relayer_address']._serialized_options = b'\362\336\037\036yaml:\"forward_relayer_address\"'
  _INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['underlying_app_success']._options = None
  _INCENTIVIZEDACKNOWLEDGEMENT.fields_by_name['underlying_app_success']._serialized_options = b'\362\336\037\036yaml:\"underlying_app_successl\"'
  _globals['_INCENTIVIZEDACKNOWLEDGEMENT']._serialized_start=85
  _globals['_INCENTIVIZEDACKNOWLEDGEMENT']._serialized_end=312
# @@protoc_insertion_point(module_scope)
