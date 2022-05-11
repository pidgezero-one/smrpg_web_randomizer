from typing import NamedTuple


class _Flag(NamedTuple):
    byte: int
    bit: int


class Flag(_Flag):
    def __new__(cls, byte: int, bit: int):
        assert 0x7040 <= byte <= 0x709F
        assert 0 <= bit <= 7
        return super().__new__(cls, byte, bit)


class ShortVar(int):
    def __new__(cls, *args, **kwargs):
        address = args[0]
        assert 0x7000 <= address <= 0x71FE and address % 2 == 0
        return super(ShortVar, cls).__new__(cls, address)


class ByteVar(int):
    def __new__(cls, *args, **kwargs):
        address = args[0]
        assert 0x70A0 <= address <= 0x719F
        return super(ByteVar, cls).__new__(cls, address)
