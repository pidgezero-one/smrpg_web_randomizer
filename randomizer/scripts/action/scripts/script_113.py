"""A0113_HENCHMAN_BOUNCING_IN_PLACE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpIfBitSet(TEMP_7043_3, ["ACTION_113_shift_west_pixels_4"]),
        FaceNortheast(),
        FixedFCoordOn(),
        SetWalkingSpeed(FASTEST),
        WalkWestPixels(1, identifier="ACTION_113_shift_west_pixels_4"),
        Pause(1),
        WalkEastPixels(1),
        Pause(1),
        Jmp(["ACTION_113_shift_west_pixels_4"]),
    ]
)
