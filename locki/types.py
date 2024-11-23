import base64

from typing import Annotated, Protocol, Union
from pydantic import PlainSerializer, PlainValidator


__all__ = (
    "SupportsLenAndGetItem",

    "b64bytes",
    "deserialize_b64bytes"
)


class SupportsLenAndGetItem[T](Protocol):
    def __len__(self) -> int: ...
    def __getitem__(self, k: int, /) -> T: ...


def deserialize_b64bytes(value: Union[bytes, str]) -> bytes:
    if isinstance(value, bytes):
        return value

    return base64.b64decode(value)


type b64bytes = Annotated[
    bytes,
    PlainSerializer(base64.b64encode, when_used="json"),
    PlainValidator(deserialize_b64bytes)
]
