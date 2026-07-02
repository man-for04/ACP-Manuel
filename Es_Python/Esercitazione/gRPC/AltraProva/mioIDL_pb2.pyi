from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class msgRichiesta(_message.Message):
    __slots__ = ("operando1", "operando2")
    OPERANDO1_FIELD_NUMBER: _ClassVar[int]
    OPERANDO2_FIELD_NUMBER: _ClassVar[int]
    operando1: int
    operando2: int
    def __init__(self, operando1: _Optional[int] = ..., operando2: _Optional[int] = ...) -> None: ...

class msgRisposta(_message.Message):
    __slots__ = ("risultato",)
    RISULTATO_FIELD_NUMBER: _ClassVar[int]
    risultato: int
    def __init__(self, risultato: _Optional[int] = ...) -> None: ...
