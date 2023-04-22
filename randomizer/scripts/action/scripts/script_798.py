"""A0798_MUSHROOM_DERBY_UNKNOWN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpIfRandom2of3(["ACTION_799_set_animation_speed_0", "ACTION_800_pause_0"]),
        SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True),
        JumpToHeight(height=80, silent=True),
        Pause(1, identifier="ACTION_798_pause_3"),
        JmpIfMarioInAir(["ACTION_798_pause_3"]),
        JumpToHeight(height=80, silent=True),
        Pause(1, identifier="ACTION_798_pause_6"),
        JmpIfMarioInAir(["ACTION_798_pause_6"]),
        JumpToHeight(height=80, silent=True),
        Pause(1, identifier="ACTION_798_pause_9"),
        JmpIfMarioInAir(["ACTION_798_pause_9"]),
        ResetProperties(),
        FaceNorthwest(),
        Return(),
    ]
)
