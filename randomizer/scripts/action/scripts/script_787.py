"""A0787_PLAYER_COWERS_IN_CORNER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 346, ["ACTION_787_set_animation_speed_10"]
        ),
        SetWalkingSpeed(VERY_FAST),
        ClearSolidityBits(cant_pass_walls=True),
        FloatingOff(),
        SetPriority(3),
        FixedFCoordOn(),
        WalkNorthwestSteps(2),
        FixedFCoordOff(),
        FaceNorthwest(),
        SetWalkingSpeed(FASTEST, identifier="ACTION_787_set_animation_speed_10"),
        SequencePlaybackOff(),
        FixedFCoordOn(),
        WalkNorthwestPixels(1, identifier="ACTION_787_shift_northwest_pixels_13"),
        WalkSoutheastPixels(1),
        Jmp(["ACTION_787_shift_northwest_pixels_13"]),
    ]
)
