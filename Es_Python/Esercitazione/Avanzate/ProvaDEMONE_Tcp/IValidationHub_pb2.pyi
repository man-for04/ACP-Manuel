from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CodeChunk(_message.Message):
    __slots__ = ("projectId", "fileName", "content", "chunkIndex")
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CHUNKINDEX_FIELD_NUMBER: _ClassVar[int]
    projectId: str
    fileName: str
    content: str
    chunkIndex: int
    def __init__(self, projectId: _Optional[str] = ..., fileName: _Optional[str] = ..., content: _Optional[str] = ..., chunkIndex: _Optional[int] = ...) -> None: ...

class ValidationResult(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...
