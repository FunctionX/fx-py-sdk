# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/genutil/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/genutil/v1beta1/genesis.proto\x12\x16\x63osmos.genutil.v1beta1\x1a\x14gogoproto/gogo.proto\"G\n\x0cGenesisState\x12\x37\n\x07gen_txs\x18\x01 \x03(\x0c\x42&\xea\xde\x1f\x06gentxs\xfa\xde\x1f\x18\x65ncoding/json.RawMessageB.Z,github.com/cosmos/cosmos-sdk/x/genutil/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.genutil.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/genutil/types'
  _GENESISSTATE.fields_by_name['gen_txs']._options = None
  _GENESISSTATE.fields_by_name['gen_txs']._serialized_options = b'\352\336\037\006gentxs\372\336\037\030encoding/json.RawMessage'
  _globals['_GENESISSTATE']._serialized_start=86
  _globals['_GENESISSTATE']._serialized_end=157
# @@protoc_insertion_point(module_scope)
