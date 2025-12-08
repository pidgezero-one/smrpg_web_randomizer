# pylint: disable=C0301

"""E3146_FREESTANDING_BIG_COIN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        PlaySound(sound=SO013_COIN, channel=4),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASClearSolidityBits(bit_4=True, cant_walk_through=True),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=False),
                ASShiftZUpSteps(2),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ]),
        AddCoins(10),
        Return(),
    ]
)
