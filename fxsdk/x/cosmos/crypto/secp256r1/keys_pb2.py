# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crypto/secp256r1/keys.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"cosmos/crypto/secp256r1/keys.proto\x12\x17\x63osmos.crypto.secp256r1\x1a\x14gogoproto/gogo.proto\"\"\n\x06PubKey\x12\x18\n\x03key\x18\x01 \x01(\x0c\x42\x0b\xda\xde\x1f\x07\x65\x63\x64saPK\"&\n\x07PrivKey\x12\x1b\n\x06secret\x18\x01 \x01(\x0c\x42\x0b\xda\xde\x1f\x07\x65\x63\x64saSKB@Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256r1\xc8\xe1\x1e\x00\xd8\xe1\x1e\x00\xc8\xe3\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crypto.secp256r1.keys_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256r1\310\341\036\000\330\341\036\000\310\343\036\001'
  _PUBKEY.fields_by_name['key']._options = None
  _PUBKEY.fields_by_name['key']._serialized_options = b'\332\336\037\007ecdsaPK'
  _PRIVKEY.fields_by_name['secret']._options = None
  _PRIVKEY.fields_by_name['secret']._serialized_options = b'\332\336\037\007ecdsaSK'
  _globals['_PUBKEY']._serialized_start=85
  _globals['_PUBKEY']._serialized_end=119
  _globals['_PRIVKEY']._serialized_start=121
  _globals['_PRIVKEY']._serialized_end=159
# @@protoc_insertion_point(module_scope)
