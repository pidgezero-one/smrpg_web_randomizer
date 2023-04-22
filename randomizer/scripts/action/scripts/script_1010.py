"""A1010_KEEP_DARK_ROOM_INIT_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(FAST),
        WalkNortheastPixels(8),
        WalkNorthwestSteps(5),
        WalkNorthwestPixels(8),
        WalkSouthwestSteps(5),
        VisibilityOff(),
        Return(),
    ]
)
