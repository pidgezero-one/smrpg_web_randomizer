"""A1003_KEEP_ORIGINAL_THRONE_ROOM_TROOPA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST, identifier="ACTION_1003_set_animation_speed_0"),
        SetWalkingSpeed(FAST),
        WalkSoutheastPixels(8),
        WalkSoutheastSteps(2),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(NORMAL),
        WalkSoutheastSteps(1),
        FaceNorthwest(),
        Pause(10),
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(FAST),
        WalkNorthwestSteps(2),
        WalkNorthwestPixels(8),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(NORMAL),
        WalkNorthwestSteps(1),
        FaceSoutheast(),
        Pause(10),
        Jmp(["ACTION_1003_set_animation_speed_0"]),
    ]
)
