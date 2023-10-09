# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/legacy/gravity/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxsdk.x.fx.legacy.gravity.v1 import tx_pb2 as fx_dot_legacy_dot_gravity_dot_v1_dot_tx__pb2
from fxsdk.x.fx.legacy.gravity.v1 import types_pb2 as fx_dot_legacy_dot_gravity_dot_v1_dot_types__pb2
from fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"fx/legacy/gravity/v1/genesis.proto\x12\rfx.gravity.v1\x1a\x1d\x66x/legacy/gravity/v1/tx.proto\x1a fx/legacy/gravity/v1/types.proto\x1a\x14gogoproto/gogo.proto\"\x99\x06\n\x06Params\x12\x12\n\ngravity_id\x18\x01 \x01(\t\x12\x1c\n\x14\x63ontract_source_hash\x18\x02 \x01(\t\x12\x1a\n\x12\x62ridge_eth_address\x18\x04 \x01(\t\x12\x17\n\x0f\x62ridge_chain_id\x18\x05 \x01(\x04\x12\x1d\n\x15signed_valsets_window\x18\x06 \x01(\x04\x12\x1d\n\x15signed_batches_window\x18\x07 \x01(\x04\x12\x1c\n\x14signed_claims_window\x18\x08 \x01(\x04\x12\x1c\n\x14target_batch_timeout\x18\n \x01(\x04\x12\x1a\n\x12\x61verage_block_time\x18\x0b \x01(\x04\x12\x1e\n\x16\x61verage_eth_block_time\x18\x0c \x01(\x04\x12M\n\x15slash_fraction_valset\x18\r \x01(\x0c\x42.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12L\n\x14slash_fraction_batch\x18\x0e \x01(\x0c\x42.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12L\n\x14slash_fraction_claim\x18\x0f \x01(\x0c\x42.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12X\n slash_fraction_conflicting_claim\x18\x10 \x01(\x0c\x42.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12&\n\x1eunbond_slashing_valsets_window\x18\x11 \x01(\x04\x12#\n\x1bibc_transfer_timeout_height\x18\x12 \x01(\x04\x12Z\n\"valset_update_power_change_percent\x18\x13 \x01(\x0c\x42.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec:\x04\x80\xdc \x00\"\xc6\x06\n\x0cGenesisState\x12+\n\x06params\x18\x01 \x01(\x0b\x32\x15.fx.gravity.v1.ParamsB\x04\xc8\xde\x1f\x00\x12\x1b\n\x13last_observed_nonce\x18\x02 \x01(\x04\x12X\n\x1alast_observed_block_height\x18\x03 \x01(\x0b\x32..fx.gravity.v1.LastObservedEthereumBlockHeightB\x04\xc8\xde\x1f\x00\x12\x45\n\rdelegate_keys\x18\x04 \x03(\x0b\x32(.fx.gravity.v1.MsgSetOrchestratorAddressB\x04\xc8\xde\x1f\x00\x12,\n\x07valsets\x18\x05 \x03(\x0b\x32\x15.fx.gravity.v1.ValsetB\x04\xc8\xde\x1f\x00\x12:\n\x0f\x65rc20_to_denoms\x18\x06 \x03(\x0b\x32\x1b.fx.gravity.v1.ERC20ToDenomB\x04\xc8\xde\x1f\x00\x12\x44\n\x13unbatched_transfers\x18\x07 \x03(\x0b\x32!.fx.gravity.v1.OutgoingTransferTxB\x04\xc8\xde\x1f\x00\x12\x35\n\x07\x62\x61tches\x18\x08 \x03(\x0b\x32\x1e.fx.gravity.v1.OutgoingTxBatchB\x04\xc8\xde\x1f\x00\x12<\n\x0e\x62\x61tch_confirms\x18\t \x03(\x0b\x32\x1e.fx.gravity.v1.MsgConfirmBatchB\x04\xc8\xde\x1f\x00\x12>\n\x0fvalset_confirms\x18\n \x03(\x0b\x32\x1f.fx.gravity.v1.MsgValsetConfirmB\x04\xc8\xde\x1f\x00\x12\x36\n\x0c\x61ttestations\x18\x0b \x03(\x0b\x32\x1a.fx.gravity.v1.AttestationB\x04\xc8\xde\x1f\x00\x12\x39\n\x14last_observed_valset\x18\x0c \x01(\x0b\x32\x15.fx.gravity.v1.ValsetB\x04\xc8\xde\x1f\x00\x12 \n\x18last_slashed_batch_block\x18\r \x01(\x04\x12!\n\x19last_slashed_valset_nonce\x18\x0e \x01(\x04\x12\x17\n\x0flast_tx_pool_id\x18\x0f \x01(\x04\x12\x15\n\rlast_batch_id\x18\x10 \x01(\x04\x42.Z,github.com/functionx/fx-core/x/gravity/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fx.legacy.gravity.v1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/functionx/fx-core/x/gravity/types'
  _PARAMS.fields_by_name['slash_fraction_valset']._options = None
  _PARAMS.fields_by_name['slash_fraction_valset']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _PARAMS.fields_by_name['slash_fraction_batch']._options = None
  _PARAMS.fields_by_name['slash_fraction_batch']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _PARAMS.fields_by_name['slash_fraction_claim']._options = None
  _PARAMS.fields_by_name['slash_fraction_claim']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _PARAMS.fields_by_name['slash_fraction_conflicting_claim']._options = None
  _PARAMS.fields_by_name['slash_fraction_conflicting_claim']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _PARAMS.fields_by_name['valset_update_power_change_percent']._options = None
  _PARAMS.fields_by_name['valset_update_power_change_percent']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _PARAMS._options = None
  _PARAMS._serialized_options = b'\200\334 \000'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['last_observed_block_height']._options = None
  _GENESISSTATE.fields_by_name['last_observed_block_height']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['delegate_keys']._options = None
  _GENESISSTATE.fields_by_name['delegate_keys']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['valsets']._options = None
  _GENESISSTATE.fields_by_name['valsets']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['erc20_to_denoms']._options = None
  _GENESISSTATE.fields_by_name['erc20_to_denoms']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['unbatched_transfers']._options = None
  _GENESISSTATE.fields_by_name['unbatched_transfers']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['batches']._options = None
  _GENESISSTATE.fields_by_name['batches']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['batch_confirms']._options = None
  _GENESISSTATE.fields_by_name['batch_confirms']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['valset_confirms']._options = None
  _GENESISSTATE.fields_by_name['valset_confirms']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['attestations']._options = None
  _GENESISSTATE.fields_by_name['attestations']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['last_observed_valset']._options = None
  _GENESISSTATE.fields_by_name['last_observed_valset']._serialized_options = b'\310\336\037\000'
  _globals['_PARAMS']._serialized_start=141
  _globals['_PARAMS']._serialized_end=934
  _globals['_GENESISSTATE']._serialized_start=937
  _globals['_GENESISSTATE']._serialized_end=1775
# @@protoc_insertion_point(module_scope)