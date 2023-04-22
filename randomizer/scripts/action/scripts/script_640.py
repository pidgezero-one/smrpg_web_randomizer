"""A0640_MIDAS_2ND_TUNNELS_PIRANHA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(3),
        SetVRAMPriority(NORMAL_PRIORITY),
        SequenceLoopingOn(),
        FixedFCoordOn(),
        StartLoopNTimes(5),
        SetAllSpeeds(NORMAL),
        Walk1StepNortheast(),
        SetSequenceSpeed(FAST),
        JumpToHeight(56),
        Pause(16),
        JumpToHeight(56),
        Pause(16),
        SetSequenceSpeed(NORMAL),
        Walk1StepSouthwest(),
        EndLoop(),
        SetAllSpeeds(FAST),
        Walk1StepNortheast(),
        Pause(1, identifier="ACTION_640_pause_17"),
        JmpIfBitClear(TEMP_7043_1, ["ACTION_640_pause_17"]),
        SetAllSpeeds(VERY_FAST),
        Walk1StepSouthwest(),
        StartLoopNTimes(7),
        ShiftZUpPixels(8),
        ShiftZDownPixels(8),
        EndLoop(),
        SetWalkingSpeed(NORMAL),
        SetSequenceSpeed(VERY_FAST),
        StartLoopNTimes(5),
        JumpToHeight(56),
        Walk1StepNortheast(),
        JumpToHeight(56),
        Walk1StepSouthwest(),
        EndLoop(),
        WalkNortheastSteps(5),
        Walk1StepEast(),
        Return(),
    ]
)
