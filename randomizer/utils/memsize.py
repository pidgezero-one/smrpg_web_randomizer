from typing import Union
from randomizer.types.overworld_scripts.variables.classes import ByteVar, ShortVar


def cast_address(address: Union[ShortVar, ByteVar]) -> Union[ShortVar, ByteVar]:
    if 0x70A0 <= address <= 0x719F:
        return ByteVar(address)
    return ShortVar(address)
