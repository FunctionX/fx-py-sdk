# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/fee/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ibc.applications.fee.v1 import fee_pb2 as ibc_dot_applications_dot_fee_dot_v1_dot_fee__pb2
from ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n ibc/applications/fee/v1/tx.proto\x12\x17ibc.applications.fee.v1\x1a\x14gogoproto/gogo.proto\x1a!ibc/applications/fee/v1/fee.proto\x1a!ibc/core/channel/v1/channel.proto\"\x8c\x01\n\x10MsgRegisterPayee\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"channel_id\"\x12\x0f\n\x07relayer\x18\x03 \x01(\t\x12\r\n\x05payee\x18\x04 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1a\n\x18MsgRegisterPayeeResponse\"\xc4\x01\n\x1cMsgRegisterCounterpartyPayee\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"channel_id\"\x12\x0f\n\x07relayer\x18\x03 \x01(\t\x12\x39\n\x12\x63ounterparty_payee\x18\x04 \x01(\tB\x1d\xf2\xde\x1f\x19yaml:\"counterparty_payee\":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"&\n$MsgRegisterCounterpartyPayeeResponse\"\xda\x01\n\x0fMsgPayPacketFee\x12/\n\x03\x66\x65\x65\x18\x01 \x01(\x0b\x32\x1c.ibc.applications.fee.v1.FeeB\x04\xc8\xde\x1f\x00\x12\x31\n\x0esource_port_id\x18\x02 \x01(\tB\x19\xf2\xde\x1f\x15yaml:\"source_port_id\"\x12\x37\n\x11source_channel_id\x18\x03 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"source_channel_id\"\x12\x0e\n\x06signer\x18\x04 \x01(\t\x12\x10\n\x08relayers\x18\x05 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x19\n\x17MsgPayPacketFeeResponse\"\xbf\x01\n\x14MsgPayPacketFeeAsync\x12J\n\tpacket_id\x18\x01 \x01(\x0b\x32\x1d.ibc.core.channel.v1.PacketIdB\x18\xf2\xde\x1f\x10yaml:\"packet_id\"\xc8\xde\x1f\x00\x12Q\n\npacket_fee\x18\x02 \x01(\x0b\x32\".ibc.applications.fee.v1.PacketFeeB\x19\xf2\xde\x1f\x11yaml:\"packet_fee\"\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1e\n\x1cMsgPayPacketFeeAsyncResponse2\xef\x03\n\x03Msg\x12m\n\rRegisterPayee\x12).ibc.applications.fee.v1.MsgRegisterPayee\x1a\x31.ibc.applications.fee.v1.MsgRegisterPayeeResponse\x12\x91\x01\n\x19RegisterCounterpartyPayee\x12\x35.ibc.applications.fee.v1.MsgRegisterCounterpartyPayee\x1a=.ibc.applications.fee.v1.MsgRegisterCounterpartyPayeeResponse\x12j\n\x0cPayPacketFee\x12(.ibc.applications.fee.v1.MsgPayPacketFee\x1a\x30.ibc.applications.fee.v1.MsgPayPacketFeeResponse\x12y\n\x11PayPacketFeeAsync\x12-.ibc.applications.fee.v1.MsgPayPacketFeeAsync\x1a\x35.ibc.applications.fee.v1.MsgPayPacketFeeAsyncResponseB7Z5github.com/cosmos/ibc-go/v6/modules/apps/29-fee/typesb\x06proto3')



_MSGREGISTERPAYEE = DESCRIPTOR.message_types_by_name['MsgRegisterPayee']
_MSGREGISTERPAYEERESPONSE = DESCRIPTOR.message_types_by_name['MsgRegisterPayeeResponse']
_MSGREGISTERCOUNTERPARTYPAYEE = DESCRIPTOR.message_types_by_name['MsgRegisterCounterpartyPayee']
_MSGREGISTERCOUNTERPARTYPAYEERESPONSE = DESCRIPTOR.message_types_by_name['MsgRegisterCounterpartyPayeeResponse']
_MSGPAYPACKETFEE = DESCRIPTOR.message_types_by_name['MsgPayPacketFee']
_MSGPAYPACKETFEERESPONSE = DESCRIPTOR.message_types_by_name['MsgPayPacketFeeResponse']
_MSGPAYPACKETFEEASYNC = DESCRIPTOR.message_types_by_name['MsgPayPacketFeeAsync']
_MSGPAYPACKETFEEASYNCRESPONSE = DESCRIPTOR.message_types_by_name['MsgPayPacketFeeAsyncResponse']
MsgRegisterPayee = _reflection.GeneratedProtocolMessageType('MsgRegisterPayee', (_message.Message,), {
  'DESCRIPTOR' : _MSGREGISTERPAYEE,
  '__module__' : 'ibc.applications.fee.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.MsgRegisterPayee)
  })
_sym_db.RegisterMessage(MsgRegisterPayee)

MsgRegisterPayeeResponse = _reflection.GeneratedProtocolMessageType('MsgRegisterPayeeResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGREGISTERPAYEERESPONSE,
  '__module__' : 'ibc.applications.fee.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.MsgRegisterPayeeResponse)
  })
_sym_db.RegisterMessage(MsgRegisterPayeeResponse)

MsgRegisterCounterpartyPayee = _reflection.GeneratedProtocolMessageType('MsgRegisterCounterpartyPayee', (_message.Message,), {
  'DESCRIPTOR' : _MSGREGISTERCOUNTERPARTYPAYEE,
  '__module__' : 'ibc.applications.fee.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.MsgRegisterCounterpartyPayee)
  })
_sym_db.RegisterMessage(MsgRegisterCounterpartyPayee)

MsgRegisterCounterpartyPayeeResponse = _reflection.GeneratedProtocolMessageType('MsgRegisterCounterpartyPayeeResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGREGISTERCOUNTERPARTYPAYEERESPONSE,
  '__module__' : 'ibc.applications.fee.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.MsgRegisterCounterpartyPayeeResponse)
  })
_sym_db.RegisterMessage(MsgRegisterCounterpartyPayeeResponse)

MsgPayPacketFee = _reflection.GeneratedProtocolMessageType('MsgPayPacketFee', (_message.Message,), {
  'DESCRIPTOR' : _MSGPAYPACKETFEE,
  '__module__' : 'ibc.applications.fee.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.MsgPayPacketFee)
  })
_sym_db.RegisterMessage(MsgPayPacketFee)

MsgPayPacketFeeResponse = _reflection.GeneratedProtocolMessageType('MsgPayPacketFeeResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGPAYPACKETFEERESPONSE,
  '__module__' : 'ibc.applications.fee.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.MsgPayPacketFeeResponse)
  })
_sym_db.RegisterMessage(MsgPayPacketFeeResponse)

MsgPayPacketFeeAsync = _reflection.GeneratedProtocolMessageType('MsgPayPacketFeeAsync', (_message.Message,), {
  'DESCRIPTOR' : _MSGPAYPACKETFEEASYNC,
  '__module__' : 'ibc.applications.fee.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.MsgPayPacketFeeAsync)
  })
_sym_db.RegisterMessage(MsgPayPacketFeeAsync)

MsgPayPacketFeeAsyncResponse = _reflection.GeneratedProtocolMessageType('MsgPayPacketFeeAsyncResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGPAYPACKETFEEASYNCRESPONSE,
  '__module__' : 'ibc.applications.fee.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.fee.v1.MsgPayPacketFeeAsyncResponse)
  })
_sym_db.RegisterMessage(MsgPayPacketFeeAsyncResponse)

_MSG = DESCRIPTOR.services_by_name['Msg']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z5github.com/cosmos/ibc-go/v6/modules/apps/29-fee/types'
  _MSGREGISTERPAYEE.fields_by_name['port_id']._options = None
  _MSGREGISTERPAYEE.fields_by_name['port_id']._serialized_options = b'\362\336\037\016yaml:\"port_id\"'
  _MSGREGISTERPAYEE.fields_by_name['channel_id']._options = None
  _MSGREGISTERPAYEE.fields_by_name['channel_id']._serialized_options = b'\362\336\037\021yaml:\"channel_id\"'
  _MSGREGISTERPAYEE._options = None
  _MSGREGISTERPAYEE._serialized_options = b'\350\240\037\000\210\240\037\000'
  _MSGREGISTERCOUNTERPARTYPAYEE.fields_by_name['port_id']._options = None
  _MSGREGISTERCOUNTERPARTYPAYEE.fields_by_name['port_id']._serialized_options = b'\362\336\037\016yaml:\"port_id\"'
  _MSGREGISTERCOUNTERPARTYPAYEE.fields_by_name['channel_id']._options = None
  _MSGREGISTERCOUNTERPARTYPAYEE.fields_by_name['channel_id']._serialized_options = b'\362\336\037\021yaml:\"channel_id\"'
  _MSGREGISTERCOUNTERPARTYPAYEE.fields_by_name['counterparty_payee']._options = None
  _MSGREGISTERCOUNTERPARTYPAYEE.fields_by_name['counterparty_payee']._serialized_options = b'\362\336\037\031yaml:\"counterparty_payee\"'
  _MSGREGISTERCOUNTERPARTYPAYEE._options = None
  _MSGREGISTERCOUNTERPARTYPAYEE._serialized_options = b'\350\240\037\000\210\240\037\000'
  _MSGPAYPACKETFEE.fields_by_name['fee']._options = None
  _MSGPAYPACKETFEE.fields_by_name['fee']._serialized_options = b'\310\336\037\000'
  _MSGPAYPACKETFEE.fields_by_name['source_port_id']._options = None
  _MSGPAYPACKETFEE.fields_by_name['source_port_id']._serialized_options = b'\362\336\037\025yaml:\"source_port_id\"'
  _MSGPAYPACKETFEE.fields_by_name['source_channel_id']._options = None
  _MSGPAYPACKETFEE.fields_by_name['source_channel_id']._serialized_options = b'\362\336\037\030yaml:\"source_channel_id\"'
  _MSGPAYPACKETFEE._options = None
  _MSGPAYPACKETFEE._serialized_options = b'\350\240\037\000\210\240\037\000'
  _MSGPAYPACKETFEEASYNC.fields_by_name['packet_id']._options = None
  _MSGPAYPACKETFEEASYNC.fields_by_name['packet_id']._serialized_options = b'\362\336\037\020yaml:\"packet_id\"\310\336\037\000'
  _MSGPAYPACKETFEEASYNC.fields_by_name['packet_fee']._options = None
  _MSGPAYPACKETFEEASYNC.fields_by_name['packet_fee']._serialized_options = b'\362\336\037\021yaml:\"packet_fee\"\310\336\037\000'
  _MSGPAYPACKETFEEASYNC._options = None
  _MSGPAYPACKETFEEASYNC._serialized_options = b'\350\240\037\000\210\240\037\000'
  _MSGREGISTERPAYEE._serialized_start=154
  _MSGREGISTERPAYEE._serialized_end=294
  _MSGREGISTERPAYEERESPONSE._serialized_start=296
  _MSGREGISTERPAYEERESPONSE._serialized_end=322
  _MSGREGISTERCOUNTERPARTYPAYEE._serialized_start=325
  _MSGREGISTERCOUNTERPARTYPAYEE._serialized_end=521
  _MSGREGISTERCOUNTERPARTYPAYEERESPONSE._serialized_start=523
  _MSGREGISTERCOUNTERPARTYPAYEERESPONSE._serialized_end=561
  _MSGPAYPACKETFEE._serialized_start=564
  _MSGPAYPACKETFEE._serialized_end=782
  _MSGPAYPACKETFEERESPONSE._serialized_start=784
  _MSGPAYPACKETFEERESPONSE._serialized_end=809
  _MSGPAYPACKETFEEASYNC._serialized_start=812
  _MSGPAYPACKETFEEASYNC._serialized_end=1003
  _MSGPAYPACKETFEEASYNCRESPONSE._serialized_start=1005
  _MSGPAYPACKETFEEASYNCRESPONSE._serialized_end=1035
  _MSG._serialized_start=1038
  _MSG._serialized_end=1533
# @@protoc_insertion_point(module_scope)