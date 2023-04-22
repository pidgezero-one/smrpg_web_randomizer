"""A0971_ENDING_CREDITS_CASTLE_SHY_GUY"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
        SetPriority(1),
        VisibilityOn(),
        SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
        Db(bytearray(b" \x04")),
        EmbeddedAnimationRoutine(
            bytearray(b"(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80")
        ),
        WalkNorthPixels(5),
        SetWalkingSpeed(SLOW),
        WalkToXYCoords(x=5, y=6),
        ShiftToXYCoords(x=5, y=8),
        SetWalkingSpeed(FASTEST),
        WalkSouthPixels(15),
        WalkSouthwestPixels(20),
        SetWalkingSpeed(SLOW),
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        WalkSouthwestSteps(3),
        WalkSouthwestPixels(8),
        Pause(8),
        Db(bytearray(b" \x05")),
        EmbeddedAnimationRoutine(
            bytearray(b"&\x00\x00\x00\x00\x00@\x80\x01\x00\x01\x00\x00\x00\x04\x80")
        ),
        Pause(511),
        Return(),
    ]
)
