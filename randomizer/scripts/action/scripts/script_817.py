"""A0817_LANDS_END_CANNON_AT_REST"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 457, ["ACTION_817_set_sprite_sequence_6"]
        ),
        SetPriority(3),
        SequenceLoopingOff(),
        FixedFCoordOn(),
        Return(),
        SetSpriteSequence(
            index=0,
            is_sequence=True,
            looping=True,
            identifier="ACTION_817_set_sprite_sequence_6",
        ),
        SequenceLoopingOff(),
        FixedFCoordOn(),
        Return(),
    ]
)
