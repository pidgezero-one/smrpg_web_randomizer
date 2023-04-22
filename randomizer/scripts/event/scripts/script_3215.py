# pylint: disable=C0301

"""E3215_SHIP_COIN_SNAKE_PUZZLE_HEADER_COIN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO088_WRONG_SIGNAL, channel=6),
        PauseActionScript(MEM_70A8),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASSetSpriteSequence(index=2, is_sequence=True, looping=False),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASShiftZUpSteps(2),
                ASVisibilityOff(),
            ],
        ),
        Return(),
    ]
)
