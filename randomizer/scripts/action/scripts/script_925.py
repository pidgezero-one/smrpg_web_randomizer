"""A0925_SPINNING_STATIC_COIN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(2, identifier="ACTION_925_set_priority_0"),
        Set700CToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 79, ["ACTION_925_set_priority_4"]),
        SetSequenceSpeed(SLOW),
        SetPriority(3, identifier="ACTION_925_set_priority_4"),
        WalkSouthPixels(3),
        SetSpriteSequence(index=1, is_sequence=True, looping=True),
        Pause(1, identifier="ACTION_925_pause_8"),
        Jmp(["ACTION_925_pause_8"]),
    ]
)
