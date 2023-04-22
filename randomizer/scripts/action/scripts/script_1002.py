"""A1002_KEEP_ORIGINAL_THRONE_ROOM_TROOPA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(NORMAL, identifier="ACTION_1002_set_animation_speed_0"),
        SetWalkingSpeed(VERY_SLOW),
        WalkNorthwestPixels(8),
        WalkNorthwestSteps(2),
        SetSequenceSpeed(SLOW),
        SetWalkingSpeed(VERY_SLOW),
        WalkNorthwestSteps(1),
        FaceSoutheast(),
        Pause(10),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(VERY_SLOW),
        WalkSoutheastSteps(2),
        WalkSoutheastPixels(8),
        SetSequenceSpeed(SLOW),
        SetWalkingSpeed(VERY_SLOW),
        WalkSoutheastSteps(1),
        FaceNorthwest(),
        Pause(10),
        Jmp(["ACTION_1002_set_animation_speed_0"]),
    ]
)
