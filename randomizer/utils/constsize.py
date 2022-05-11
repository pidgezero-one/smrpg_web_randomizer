from typing import Union
from randomizer.types.numbers.classes import UInt16, UInt8


def cast_const(value: Union[UInt16, UInt8]) -> Union[UInt16, UInt8]:
    if 0 <= value <= 0xFF:
        return UInt8(value)
    return UInt16(value)
