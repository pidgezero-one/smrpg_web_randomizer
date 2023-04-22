"""A0470_COLLECT_MIDAS_COIN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Db(bytearray(b"\xfd\xf2")),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        PlaySound(sound=SO013_COIN, channel=4),
        SetVRAMPriority(PRIORITY_3),
        SetPriority(3),
        SetSpriteSequence(index=2, looping=False),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(VERY_FAST),
        AddZCoord1Step(),
        Pause(26),
        VisibilityOff(),
        Return(),
    ]
)
