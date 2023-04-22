"""A0088_SHOP_TADPOLE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetBit(TEMP_7043_5),
        ShiftToXYCoords(x=7, y=40),
        VisibilityOn(),
        SetSequenceSpeed(FAST),
        PlaySound(sound=SO050_WATER_DROPLET, channel=4),
        SetSpriteSequence(index=10, is_sequence=True, looping=True),
        Pause(12),
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        SetWalkingSpeed(FAST),
        WalkSouthwestSteps(1),
        SetWalkingSpeed(NORMAL),
        WalkSouthwestPixels(8),
        SetWalkingSpeed(SLOW),
        WalkSouthwestPixels(5),
        Jmp(["ACTION_154_fixed_f_coord_on_0"]),
    ]
)
