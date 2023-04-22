"""A0604_MIDAS_1ST_TUNNEL_SPINY"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(3, identifier="ACTION_604_set_priority_0"),
        SetAllSpeeds(NORMAL),
        Walk1StepSouthwest(),
        Walk1StepNorthwest(),
        Pause(20),
        SetAllSpeeds(FAST),
        Walk1StepEast(),
        Pause(13),
        Jmp(["ACTION_604_set_priority_0"]),
    ]
)
