from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class msg_req(_message.Message):
    __slots__ = ("task", "tipo")
    TASK_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    task: str
    tipo: str
    def __init__(self, task: _Optional[str] = ..., tipo: _Optional[str] = ...) -> None: ...

class msg_res(_message.Message):
    __slots__ = ("ritorno",)
    RITORNO_FIELD_NUMBER: _ClassVar[int]
    ritorno: str
    def __init__(self, ritorno: _Optional[str] = ...) -> None: ...
