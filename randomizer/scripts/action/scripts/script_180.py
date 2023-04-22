"""A0180_FOREST_1ST_UNDERGROUND_RAT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(identifier="ACTION_180_sequence_looping_on_0"),
        ClearSolidityBits(cant_pass_walls=True),
        SetSequenceSpeed(FAST),
        WalkSoutheastSteps(6),
        Pause(24),
        FaceSouthwest(),
        Pause(24),
        FaceNortheast(),
        Pause(24),
        FaceSoutheast(),
        Pause(24),
        WalkSouthwestSteps(2),
        WalkNorthwestSteps(8),
        Walk1StepNortheast(),
        WalkNorthwestSteps(8),
        WalkSouthwestSteps(3),
        Pause(24),
        FaceNorthwest(),
        Pause(24),
        FaceSoutheast(),
        Pause(24),
        WalkNortheastSteps(4),
        WalkSoutheastSteps(10),
        Jmp(["ACTION_180_sequence_looping_on_0"]),
    ]
)
