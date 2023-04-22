"""A0984_DREAM_CUSHION_CHEF"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(SLOW),
        SequenceLoopingOn(),
        Pause(1, identifier="ACTION_984_pause_2"),
        JmpIfBitSet(TEMP_7043_1, ["ACTION_984_face_southwest_5"]),
        Jmp(["ACTION_984_pause_2"]),
        FaceSouthwest(identifier="ACTION_984_face_southwest_5"),
        Pause(30),
        FaceSoutheast(),
        Pause(30),
        SetSequenceSpeed(NORMAL),
        SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
        Pause(40),
        SetSequenceSpeed(SLOW),
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        Jmp(["ACTION_984_pause_2"]),
    ]
)
