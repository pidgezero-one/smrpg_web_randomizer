"""A1000_KEEP_ORIGINAL_THRONE_ROOM_TROOPA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST, identifier="ACTION_1000_set_animation_speed_0"),
        SetWalkingSpeed(NORMAL),
        WalkSoutheastPixels(8),
        WalkSoutheastSteps(2),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(SLOW),
        WalkSoutheastSteps(1),
        FaceNorthwest(),
        Pause(10),
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(NORMAL),
        WalkNorthwestSteps(2),
        WalkNorthwestPixels(8),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(SLOW),
        WalkNorthwestSteps(1),
        FaceSoutheast(),
        Pause(10),
        Jmp(["ACTION_1000_set_animation_speed_0"]),
    ]
)
