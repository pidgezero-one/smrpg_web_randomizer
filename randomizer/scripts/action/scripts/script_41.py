"""A0041_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_LEFT_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(
            index=4, looping=False, identifier="ACTION_41_set_sprite_sequence_0"
        ),
        Pause(40),
        Jmp(["ACTION_41_set_sprite_sequence_0"]),
    ]
)
