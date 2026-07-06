from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Richiesta_temperatura(_message.Message):
    __slots__ = ("temperatura",)
    TEMPERATURA_FIELD_NUMBER: _ClassVar[int]
    temperatura: int
    def __init__(self, temperatura: _Optional[int] = ...) -> None: ...

class Risposta_string(_message.Message):
    __slots__ = ("msg",)
    MSG_FIELD_NUMBER: _ClassVar[int]
    msg: str
    def __init__(self, msg: _Optional[str] = ...) -> None: ...

class Richiesta_vuota(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Risposta_float(_message.Message):
    __slots__ = ("media",)
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    media: float
    def __init__(self, media: _Optional[float] = ...) -> None: ...
