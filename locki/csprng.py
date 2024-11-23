import secrets

from .types import SupportsLenAndGetItem


__all__ = (
    "generate_random_bytes",
    "generate_random_choice"
)


def generate_random_bytes(length: int) -> bytes:
    return secrets.token_bytes(length)


def generate_random_choice[T](items: SupportsLenAndGetItem[T]) -> T:
    return secrets.choice(items)
