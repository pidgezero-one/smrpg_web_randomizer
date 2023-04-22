"""A0042_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_RIGHT_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(
            index=4,
            looping=False,
            mirror_sprite=True,
            identifier="ACTION_42_set_sprite_sequence_0",
        ),
        Pause(40),
        Jmp(["ACTION_42_set_sprite_sequence_0"]),
    ]
)
