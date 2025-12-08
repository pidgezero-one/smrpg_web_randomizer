"""A0861_ABYSS_1ST_BOSS_FIGHT_SHOCKED"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(
            index=0,
            sprite_offset=3,
            is_sequence=True,
            looping=True,
            identifier="ACTION_861_set_sprite_sequence_0"),
        Pause(16),
        SetSpriteSequence(
            index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(16),
        Jmp(["ACTION_861_set_sprite_sequence_0"]),
    ]
)
