"""A0250_DRILL_BIT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOff(),
        FaceSoutheast(),
        TransferToXYZF(x=4, y=19, z=0, direction=EAST),
        TransferXYZFPixels(x=12, y=12, z=0, direction=EAST),
        ShadowOn(),
        VisibilityOn(),
        SetSpriteSequence(
            index=9, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(6),
        SetSpriteSequence(
            index=8, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(6),
        SetSpriteSequence(
            index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(6),
        SetSpriteSequence(
            index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(6),
        ResetProperties(),
        SetSequenceSpeed(FAST),
        SequencePlaybackOn(),
        WalkSoutheastSteps(5),
        SequencePlaybackOff(),
        AddZCoord1Step(),
        SetWalkingSpeed(FAST),
        ShiftZUpSteps(2),
        SetWalkingSpeed(VERY_FAST),
        SetBit(TEMP_7044_4),
        ShiftZUpSteps(2),
        SetWalkingSpeed(FASTEST),
        ShiftZUpSteps(4),
        ShadowOff(),
        SetWalkingSpeed(NORMAL),
        TransferToXYZF(x=3, y=48, z=0, direction=EAST),
        SetBit(TEMP_7044_4),
        Return(),
    ]
)
