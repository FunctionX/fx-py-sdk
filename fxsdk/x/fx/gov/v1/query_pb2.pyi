from fxsdk.x.fx.gov.v1 import params_pb2 as _params_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryParamsRequest(_message.Message):
    __slots__ = ["msg_type"]
    MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
    msg_type: str
    def __init__(self, msg_type: _Optional[str] = ...) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _params_pb2.Params
    def __init__(self, params: _Optional[_Union[_params_pb2.Params, _Mapping]] = ...) -> None: ...

class QueryEGFParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryEGFParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _params_pb2.EGFParams
    def __init__(self, params: _Optional[_Union[_params_pb2.EGFParams, _Mapping]] = ...) -> None: ...
