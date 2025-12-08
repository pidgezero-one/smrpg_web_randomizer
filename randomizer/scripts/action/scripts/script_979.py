"""A0979_NIMBUS_CASTLE_CAGED_BIRD"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShadowOff(),
        SetPriority(3),
        SetWalkingSpeed(SLOW),
        TransferXYZFPixels(x=251, y=254, z=5, direction=EAST),
        SetSpriteSequence(
            index=0,
            is_sequence=True,
            looping=True,
            identifier="ACTION_979_set_sprite_sequence_4"),
        Pause(10),
        ShiftZUpPixels(8),
        ShiftZDownPixels(8),
        SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
        JmpIfRandom1of2(["ACTION_979_pause_11"]),
        Pause(60),
        Pause(60, identifier="ACTION_979_pause_11"),
        JmpIfRandom1of2(["ACTION_980_pause_4"]),
        Jmp(["ACTION_979_set_sprite_sequence_4"]),
    ]
)
