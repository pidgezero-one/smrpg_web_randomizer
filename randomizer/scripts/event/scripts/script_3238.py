# pylint: disable=C0301

"""E3238_FREESTANDING_FROG_COIN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        RemoveObjectAt70A8FromCurrentLevel(),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASClearSolidityBits(bit_4=True, cant_walk_through=True),
                ASPlaySound(sound=SO094_FROG_COIN, channel=4),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=False),
                ASSetWalkingSpeed(SLOW),
                ASShiftZUpSteps(2),
                ASVisibilityOff(),
                ASReturn(),
            ]),
        AddFrogCoins(1),
        Return(),
    ]
)
