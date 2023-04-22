"""A0533_MUSHROOM_WAY_1_TROOPA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Db(bytearray(b" \x04")),
        EmbeddedAnimationRoutine(
            bytearray(b"(\x00\x00\x00\x00\x00@\x00\x06\x00\x01\x00\x00\x00\x04\x80")
        ),
        SetSequenceSpeed(FAST, identifier="ACTION_533_set_animation_speed_2"),
        SetWalkingSpeed(NORMAL),
        WalkNortheastSteps(1),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(SLOW),
        WalkNortheastSteps(1),
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(NORMAL),
        WalkSoutheastSteps(1),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(SLOW),
        WalkSoutheastSteps(1),
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(NORMAL),
        WalkSouthwestSteps(1),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(SLOW),
        WalkSouthwestSteps(1),
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(NORMAL),
        WalkNorthwestSteps(1),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(SLOW),
        WalkNorthwestSteps(1),
        Jmp(["ACTION_533_set_animation_speed_2"]),
    ]
)
