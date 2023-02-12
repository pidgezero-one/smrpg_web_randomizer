# E1293_COLLECT_FREESTANDING_SMALL_COIN

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        AddCoins(1),
        DisableObjectTrigger(MEM_70A8),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASSetSpriteSequence(index=2, looping=False),
                ASSetWalkingSpeed(NORMAL),
                ASPlaySound(sound=SO013_COIN, channel=6),
                ASShiftZUpSteps(2),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        Return(),
    ]
)
