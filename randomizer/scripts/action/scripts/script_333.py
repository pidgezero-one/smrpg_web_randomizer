"""A0333_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_ITEM_PATH"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOn(),
        JmpToSubroutine(["ACTION_15_ret_0"]),
        Pause(117),
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_4_PRIZE, ["script_333_reset"]),
        JumpToHeight(108),
        WalkSouthwestSteps(2),
        StartLoopNTimes(4),
        VisibilityOn(),
        Pause(2),
        VisibilityOff(),
        Pause(2),
        EndLoop(),
        Return(),
        ResetProperties(identifier="script_333_reset"),
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(FASTER),
        Walk1StepEast(),
        Walk1StepWest(),
        Jmp(["script_333_reset"]),
    ]
)
