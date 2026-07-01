from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class msgInvio(_message.Message):
    __slots__ = ("contenuto",)
    CONTENUTO_FIELD_NUMBER: _ClassVar[int]
    contenuto: str
    def __init__(self, contenuto: _Optional[str] = ...) -> None: ...

class msgRitorno(_message.Message):
    __slots__ = ("contenuto",)
    CONTENUTO_FIELD_NUMBER: _ClassVar[int]
    contenuto: str
    def __init__(self, contenuto: _Optional[str] = ...) -> None: ...
