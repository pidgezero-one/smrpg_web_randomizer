"""A0081_MELODY_BAY_TUTORIAL"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST),
        VisibilityOn(),
        JmpIfBitSet(TEMP_7044_6, ["ACTION_81_set_sprite_sequence_4"]),
        PlaySound(sound=SO050_WATER_DROPLET, channel=4),
        SetSpriteSequence(
            index=10,
            is_sequence=True,
            looping=True,
            identifier="ACTION_81_set_sprite_sequence_4"),
        Pause(12),
        SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
        Jmp(["ACTION_154_fixed_f_coord_on_0"]),
        Return(),
    ]
)
