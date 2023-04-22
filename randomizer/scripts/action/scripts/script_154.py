"""A0154_TADPOLE_POND_TADPOLE_DEFAULT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FixedFCoordOn(identifier="ACTION_154_fixed_f_coord_on_0"),
        SetSequenceSpeed(FAST),
        SequenceLoopingOn(),
        SetWalkingSpeed(SLOW),
        WalkWestPixels(1),
        Pause(1),
        SetWalkingSpeed(VERY_SLOW),
        WalkNorthwestPixels(1),
        Pause(1),
        SetWalkingSpeed(VERY_SLOW),
        WalkSoutheastPixels(1),
        Pause(1),
        SetWalkingSpeed(VERY_SLOW),
        WalkEastPixels(1),
        Pause(1),
        SetWalkingSpeed(SLOW),
        WalkEastPixels(1),
        Pause(1),
        SetWalkingSpeed(VERY_SLOW),
        WalkNortheastPixels(1),
        Pause(1),
        SetWalkingSpeed(VERY_SLOW),
        WalkSouthwestPixels(1),
        Pause(1),
        SetWalkingSpeed(VERY_SLOW),
        WalkWestPixels(1),
        Pause(1),
        Jmp(["ACTION_154_fixed_f_coord_on_0"]),
    ]
)
