from . import csprng


_RECOVERY_CODE_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


__all__ = (
    "generate_random_recovery_code",
)


def _generate_random_recovery_code_segment(length: int) -> str:
    return "".join(
        csprng.generate_random_choice(_RECOVERY_CODE_ALPHABET)
        for _ in range(length)
    )


def generate_random_recovery_code(
    *,
    segments: int,
    segment_length: int
) -> str:
    return "-".join(
        _generate_random_recovery_code_segment(segment_length)
        for _ in range(segments)
    )
