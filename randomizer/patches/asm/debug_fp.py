"""Debug mode: start the run with FP at 99 (current and max).

Writes 1 byte each at ROM $3A:00DD (current FP) and ROM
$3A:00DE (maximum FP). Caller should only invoke this when
settings.debug_mode is true.
"""


def get_patch() -> dict[int, bytes]:
    return {
        0x3A00DD: bytes([99]),
        0x3A00DE: bytes([99]),
    }
