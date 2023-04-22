"""A0892_KNIFE_GUY_DEFAULT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(),
        SetSequenceSpeed(NORMAL),
        SetSpriteSequence(
            index=0, looping=True, identifier="ACTION_892_set_sprite_sequence_2"
        ),
        Pause(32),
        SetSpriteSequence(index=1, looping=True),
        Pause(32),
        Jmp(["ACTION_892_set_sprite_sequence_2"]),
    ]
)
