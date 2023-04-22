"""A0044_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_CHOW"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Pause(55),
        FixedFCoordOn(),
        SequenceLoopingOn(),
        SetWalkingSpeed(VERY_SLOW),
        SetSequenceSpeed(VERY_FAST),
        WalkNortheastPixels(8, identifier="ACTION_44_shift_northeast_pixels_5"),
        Pause(20),
        SetWalkingSpeed(FAST),
        SetSequenceSpeed(SLOW),
        JumpToHeight(height=40, silent=True),
        WalkSouthwestPixels(12),
        Pause(25),
        SetWalkingSpeed(VERY_SLOW),
        SetSequenceSpeed(VERY_FAST),
        WalkNortheastPixels(4),
        Jmp(["ACTION_44_shift_northeast_pixels_5"]),
    ]
)
