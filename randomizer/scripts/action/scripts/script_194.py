"""A0194_BEAN_VALLEY_CHOMP"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(
            index=0,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_194_set_sprite_sequence_0",
        ),
        Pause(5, identifier="ACTION_194_pause_1"),
        JmpIfObjectWithinRangeSameZ(
            comparing_npc=MARIO,
            usually=0,
            tiles=4,
            destinations=["ACTION_194_set_sprite_sequence_4"],
        ),
        Jmp(["ACTION_194_pause_1"]),
        SetSpriteSequence(
            index=3,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_194_set_sprite_sequence_4",
        ),
        Pause(5, identifier="ACTION_194_pause_5"),
        JmpIfObjectWithinRangeSameZ(
            comparing_npc=MARIO, usually=0, tiles=4, destinations=["ACTION_194_pause_5"]
        ),
        Jmp(["ACTION_194_set_sprite_sequence_0"]),
    ]
)
