from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Sensor(_message.Message):
    __slots__ = ("id", "data_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    data_type: str
    def __init__(self, id: _Optional[int] = ..., data_type: _Optional[str] = ...) -> None: ...

class MeanRequest(_message.Message):
    __slots__ = ("id", "data_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    data_type: str
    def __init__(self, id: _Optional[int] = ..., data_type: _Optional[str] = ...) -> None: ...

class StringMessage(_message.Message):
    __slots__ = ("media",)
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    media: float
    def __init__(self, media: _Optional[float] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
