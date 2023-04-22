"""A0532_MUSHROOM_WAY_1_TROOPA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Db(bytearray(b" \x04")),
        EmbeddedAnimationRoutine(
            bytearray(b"(\x00\x00\x00\x00\x00@\x00\x06\x00\x01\x00\x00\x00\x04\x80")
        ),
        SetSequenceSpeed(FAST, identifier="ACTION_532_set_animation_speed_2"),
        SetWalkingSpeed(NORMAL),
        WalkSouthwestSteps(7),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(SLOW),
        WalkSouthwestSteps(1),
        SetSequenceSpeed(SLOW),
        SetWalkingSpeed(VERY_SLOW),
        WalkSouthwestSteps(1),
        Pause(30),
        FaceSoutheast(),
        Pause(5),
        FaceNortheast(),
        Pause(30),
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(NORMAL),
        WalkNortheastSteps(7),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(SLOW),
        WalkNortheastSteps(1),
        SetSequenceSpeed(SLOW),
        SetWalkingSpeed(VERY_SLOW),
        WalkNortheastSteps(1),
        Pause(30),
        FaceNorthwest(),
        Pause(5),
        FaceSouthwest(),
        Pause(30),
        Jmp(["ACTION_532_set_animation_speed_2"]),
    ]
)
