"""A0555_BOOSTER_PASS_TOSSED_SPINY"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOff(),
        SetBit(TEMP_7043_7),
        SequenceLoopingOn(),
        Db(bytearray(b"\xfd\x12")),
        SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True),
        Db(bytearray(b"\xc8\x98")),
        Db(bytearray(b"\x9a")),
        SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
        VisibilityOn(),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        JumpToHeight(48),
        Walk1StepNorthwest(),
        SetVRAMPriority(NORMAL_PRIORITY),
        Pause(1),
        SetSpriteSequence(index=3, looping=False),
        Pause(45),
        ClearBit(TEMP_7043_7),
        Jmp(["ACTION_404_face_mario_3"]),
    ]
)
