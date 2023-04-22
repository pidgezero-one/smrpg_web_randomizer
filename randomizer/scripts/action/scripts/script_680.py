"""A0680_MUSHROOM_DERBY_UNKNOWN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(),
        SetSequenceSpeed(SLOW),
        Pause(8, identifier="ACTION_680_pause_2"),
        SetSpriteSequence(
            index=21, sprite_offset=2, is_mold=True, is_sequence=True, looping=True
        ),
        Pause(8),
        ResetProperties(),
        Pause(1, identifier="ACTION_680_pause_6"),
        JmpIfBitSet(TEMP_7043_1, ["ACTION_680_ret_11"]),
        JmpIfMarioInAir(["ACTION_680_pause_6"]),
        Pause(30),
        Jmp(["ACTION_680_pause_2"]),
        Return(identifier="ACTION_680_ret_11"),
    ]
)
