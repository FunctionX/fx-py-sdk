# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/ibc/applications/transfer/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxpysdk.fxsdk.x.ibc.applications.transfer.v1 import query_pb2 as ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+fx/ibc/applications/transfer/v1/query.proto\x12\x1f\x66x.ibc.applications.transfer.v1\x1a(ibc/applications/transfer/v1/query.proto2\xf6\x04\n\x05Query\x12{\n\nDenomTrace\x12\x34.ibc.applications.transfer.v1.QueryDenomTraceRequest\x1a\x35.ibc.applications.transfer.v1.QueryDenomTraceResponse\"\x00\x12~\n\x0b\x44\x65nomTraces\x12\x35.ibc.applications.transfer.v1.QueryDenomTracesRequest\x1a\x36.ibc.applications.transfer.v1.QueryDenomTracesResponse\"\x00\x12o\n\x06Params\x12\x30.ibc.applications.transfer.v1.QueryParamsRequest\x1a\x31.ibc.applications.transfer.v1.QueryParamsResponse\"\x00\x12x\n\tDenomHash\x12\x33.ibc.applications.transfer.v1.QueryDenomHashRequest\x1a\x34.ibc.applications.transfer.v1.QueryDenomHashResponse\"\x00\x12\x84\x01\n\rEscrowAddress\x12\x37.ibc.applications.transfer.v1.QueryEscrowAddressRequest\x1a\x38.ibc.applications.transfer.v1.QueryEscrowAddressResponse\"\x00\x42@Z>github.com/functionx/fx-core/x/ibc/applications/transfer/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fx.ibc.applications.transfer.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z>github.com/functionx/fx-core/x/ibc/applications/transfer/types'
  _globals['_QUERY']._serialized_start=123
  _globals['_QUERY']._serialized_end=753
# @@protoc_insertion_point(module_scope)
