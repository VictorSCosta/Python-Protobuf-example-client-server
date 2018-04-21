# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mensagem.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mensagem.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0emensagem.proto\"\xcc\x02\n\x08Mensagem\x12\x12\n\nid_cliente\x18\x01 \x02(\x05\x12\x13\n\x0bid_mensagem\x18\x02 \x02(\x05\x12\r\n\x05\x64\x61\x64os\x18\x03 \x02(\t\x12\x0c\n\x04hmac\x18\x04 \x02(\t\x12\x13\n\x0bsender_name\x18\x05 \x02(\t\x12\x14\n\x0csender_email\x18\x06 \x02(\t\x12\x17\n\x0fsender_nickname\x18\x07 \x02(\t\x12\x15\n\rreceiver_name\x18\x08 \x02(\t\x12\x16\n\x0ereceiver_email\x18\t \x02(\t\x12\x19\n\x11receiver_nickname\x18\n \x02(\t\x12$\n\x08msg_type\x18\x0b \x02(\x0e\x32\x12.Mensagem.Msg_type\x12\x11\n\tthread_id\x18\x0c \x01(\x03\x12\x0f\n\x07subject\x18\r \x02(\t\"\"\n\x08Msg_type\x12\x0b\n\x07REQUEST\x10\x00\x12\t\n\x05REPLY\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_MENSAGEM_MSG_TYPE = _descriptor.EnumDescriptor(
  name='Msg_type',
  full_name='Mensagem.Msg_type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REQUEST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLY', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=317,
  serialized_end=351,
)
_sym_db.RegisterEnumDescriptor(_MENSAGEM_MSG_TYPE)


_MENSAGEM = _descriptor.Descriptor(
  name='Mensagem',
  full_name='Mensagem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_cliente', full_name='Mensagem.id_cliente', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id_mensagem', full_name='Mensagem.id_mensagem', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dados', full_name='Mensagem.dados', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hmac', full_name='Mensagem.hmac', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender_name', full_name='Mensagem.sender_name', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender_email', full_name='Mensagem.sender_email', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender_nickname', full_name='Mensagem.sender_nickname', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receiver_name', full_name='Mensagem.receiver_name', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receiver_email', full_name='Mensagem.receiver_email', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receiver_nickname', full_name='Mensagem.receiver_nickname', index=9,
      number=10, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_type', full_name='Mensagem.msg_type', index=10,
      number=11, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thread_id', full_name='Mensagem.thread_id', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subject', full_name='Mensagem.subject', index=12,
      number=13, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MENSAGEM_MSG_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=351,
)

_MENSAGEM.fields_by_name['msg_type'].enum_type = _MENSAGEM_MSG_TYPE
_MENSAGEM_MSG_TYPE.containing_type = _MENSAGEM
DESCRIPTOR.message_types_by_name['Mensagem'] = _MENSAGEM

Mensagem = _reflection.GeneratedProtocolMessageType('Mensagem', (_message.Message,), dict(
  DESCRIPTOR = _MENSAGEM,
  __module__ = 'mensagem_pb2'
  # @@protoc_insertion_point(class_scope:Mensagem)
  ))
_sym_db.RegisterMessage(Mensagem)


# @@protoc_insertion_point(module_scope)