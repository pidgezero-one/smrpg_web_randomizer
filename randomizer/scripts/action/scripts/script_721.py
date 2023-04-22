"""A0721_SEQUENCE_2_STATIC"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOff(),
        SetSpriteSequence(index=2, is_sequence=True, looping=True),
        SequenceLoopingOn(),
        SetPriority(3),
        VisibilityOn(),
        SetSolidityBits(cant_jump_through=True),
        Pause(1, identifier="ACTION_721_pause_8"),
        Jmp(["ACTION_721_pause_8"]),
    ]
)
