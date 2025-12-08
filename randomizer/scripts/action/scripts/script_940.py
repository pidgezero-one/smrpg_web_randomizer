"""A0940_TELEPORTATION_SHINE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        PlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=4),
        JmpIfBitSet(TEMP_7044_0, ["ACTION_940_set_sprite_sequence_5"]),
        SetSpriteSequence(index=0, is_sequence=True, looping=False),
        Pause(8),
        Return(),
        SetSpriteSequence(
            index=1,
            is_sequence=True,
            looping=False,
            identifier="ACTION_940_set_sprite_sequence_5"),
        Pause(8),
        Return(),
    ]
)
