"""Base classes for in-game variables that are used by event and action scripts."""

from typing import NamedTuple


class _Flag(NamedTuple):
    byte: int
    bit: int


class Flag(_Flag):
    """An in-game variable that is a single true/false bit,
    normally carrying meaning independent of the byte it belongs to.\n
    Bits for 8-bit addresses between 0x7040 and 0x709F can be used for this."""

    def __new__(cls, byte: int, bit: int):
        assert 0x7040 <= byte <= 0x709F
        assert 0 <= bit <= 7
        return super().__new__(cls, byte, bit)


class ShortVar(int):
    """An in-game variable that can store 16-bit short int values.\n
    Addresses between 0x7000 and 0x71FE can be used for this."""

    def __new__(cls, *args):
        address = args[0]
        assert 0x7000 <= address <= 0x71FE and address % 2 == 0
        return super(ShortVar, cls).__new__(cls, address)

    def to_byte(self) -> int:
        """Casts the variable address to a byte value to be used
        when writing the ROM patch, understood by the game."""
        byte = (self - 0x7000) // 2
        assert 0 <= byte <= 0xFF
        return byte


class ByteVar(int):
    """An in-game variable that can store 8-bit byte int values.\n
    Addresses between 0x7040 and 0x719F can be used for this."""

    def __new__(cls, *args):
        address = args[0]
        assert 0x7040 <= address <= 0x719F
        return super(ByteVar, cls).__new__(cls, address)

    def to_byte(self) -> int:
        """Casts the variable address to a byte value to be used
        when writing the ROM patch, understood by the game."""
        byte = self - 0x70A0
        assert 0 <= byte <= 0xFF
        return byte
