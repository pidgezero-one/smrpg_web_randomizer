"""A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        SequenceLoopingOn(),
        SetSequenceSpeed(FAST),
        SetSpriteSequence(index=1, is_sequence=True, looping=False),
        Db(bytearray(b" \x04")),
        Db(bytearray(b"%\xc0\x03\x80\xff")),
        Pause(8),
        BPL262728(),
        SetSpriteSequence(index=2, is_sequence=True, looping=True),
        Pause(24),
        SetSpriteSequence(index=3, is_sequence=True, looping=False),
        Db(bytearray(b" \x04")),
        Db(bytearray(b"%@\x00\x80\xff")),
        Pause(8),
        BPL262728(),
        SetSpriteSequence(index=4, is_sequence=True, looping=False),
        SequenceLoopingOff(),
        Return(),
    ]
)
