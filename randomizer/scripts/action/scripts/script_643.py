"""A0643_MIDAS_2ND_TUNNELS_FISH"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(),
        SetPriority(3),
        SetWalkingSpeed(SLOW),
        JmpIfBitSet(
            MIDAS_RIVER_TUNNEL_2_DIRECTION, ["ACTION_643_shift_southeast_steps_24"]
        ),
        Pause(173),
        StartLoopNTimes(4),
        WalkSoutheastSteps(2),
        WalkNorthwestSteps(2),
        EndLoop(),
        StartLoopNTimes(3),
        TurnClockwise45DegreesNTimes(6),
        Pause(3),
        EndLoop(),
        WalkSoutheastSteps(6),
        JumpToHeight(120),
        SetAllSpeeds(FAST),
        FixedFCoordOn(),
        SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True),
        WalkNortheastSteps(2),
        Pause(7),
        FloatingOff(),
        SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
        SetBit(TEMP_7043_3),
        Return(),
        WalkSoutheastSteps(2, identifier="ACTION_643_shift_southeast_steps_24"),
        WalkNorthwestSteps(2),
        Jmp(["ACTION_643_shift_southeast_steps_24"]),
    ]
)
