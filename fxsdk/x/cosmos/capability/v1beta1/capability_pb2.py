# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/capability/v1beta1/capability.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*cosmos/capability/v1beta1/capability.proto\x12\x19\x63osmos.capability.v1beta1\x1a\x14gogoproto/gogo.proto\"!\n\nCapability\x12\r\n\x05index\x18\x01 \x01(\x04:\x04\x98\xa0\x1f\x00\"/\n\x05Owner\x12\x0e\n\x06module\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"J\n\x10\x43\x61pabilityOwners\x12\x36\n\x06owners\x18\x01 \x03(\x0b\x32 .cosmos.capability.v1beta1.OwnerB\x04\xc8\xde\x1f\x00\x42\x31Z/github.com/cosmos/cosmos-sdk/x/capability/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.capability.v1beta1.capability_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/github.com/cosmos/cosmos-sdk/x/capability/types'
  _CAPABILITY._options = None
  _CAPABILITY._serialized_options = b'\230\240\037\000'
  _OWNER._options = None
  _OWNER._serialized_options = b'\210\240\037\000\230\240\037\000'
  _CAPABILITYOWNERS.fields_by_name['owners']._options = None
  _CAPABILITYOWNERS.fields_by_name['owners']._serialized_options = b'\310\336\037\000'
  _globals['_CAPABILITY']._serialized_start=95
  _globals['_CAPABILITY']._serialized_end=128
  _globals['_OWNER']._serialized_start=130
  _globals['_OWNER']._serialized_end=177
  _globals['_CAPABILITYOWNERS']._serialized_start=179
  _globals['_CAPABILITYOWNERS']._serialized_end=253
# @@protoc_insertion_point(module_scope)
