from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Msg_labnumber(_message.Message):
    __slots__ = ("lab_number",)
    LAB_NUMBER_FIELD_NUMBER: _ClassVar[int]
    lab_number: int
    def __init__(self, lab_number: _Optional[int] = ...) -> None: ...

class Ack(_message.Message):
    __slots__ = ("ack",)
    ACK_FIELD_NUMBER: _ClassVar[int]
    ack: bool
    def __init__(self, ack: bool = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
