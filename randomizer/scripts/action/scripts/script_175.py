"""A0175_MIDAS_UPPER_TUNNEL_TROOPA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(),
        SetPriority(3),
        SetSpriteSequence(
            index=4,
            is_sequence=True,
            looping=True,
            identifier="ACTION_175_set_sprite_sequence_2",
        ),
        Pause(29),
        ResetProperties(),
        Pause(20),
        Jmp(["ACTION_175_set_sprite_sequence_2"]),
    ]
)
