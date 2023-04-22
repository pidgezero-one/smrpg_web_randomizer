"""A0802_MUSHROOM_DERBY_UNKNOWN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceSouthwest(),
        FixedFCoordOn(),
        SequenceLoopingOn(),
        JmpIfRandom1of2(["ACTION_802_fixed_f_coord_off_18"]),
        WalkNortheastPixels(8),
        SequenceLoopingOff(),
        SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True),
        Pause(4),
        SetWalkingSpeed(FASTEST),
        WalkSouthwestPixels(8),
        SetSpriteSequence(index=1, sprite_offset=3, is_sequence=True, looping=True),
        Pause(30),
        ResetProperties(),
        SetWalkingSpeed(FAST),
        Pause(10),
        SetSpriteSequence(index=8, is_sequence=True, looping=True),
        Pause(30),
        ResetProperties(),
        FixedFCoordOff(identifier="ACTION_802_fixed_f_coord_off_18"),
        Walk1StepEast(),
        Walk1StepNorth(),
        ClearSolidityBits(cant_pass_walls=True),
        WalkNortheastSteps(4),
        WalkNortheastPixels(4),
        WalkNorthwestSteps(4),
        SequenceLoopingOff(),
        FaceSouthwest(),
        SetSolidityBits(cant_pass_walls=True),
        Return(),
    ]
)
