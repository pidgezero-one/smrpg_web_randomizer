"""A0856_GARDENER_RUNS_IN_CIRCLES"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(VERY_FAST),
        Walk1StepSoutheast(identifier="ACTION_856_walk_1_step_southeast_1"),
        WalkSouthwestSteps(2),
        WalkNorthwestSteps(2),
        WalkNortheastSteps(2),
        Walk1StepSoutheast(),
        JmpIfBitSet(TEMP_7043_0, ["ACTION_856_face_northeast_8"]),
        Jmp(["ACTION_856_walk_1_step_southeast_1"]),
        FaceNortheast(identifier="ACTION_856_face_northeast_8"),
        SetWalkingSpeed(NORMAL),
        SetBit(TEMP_7043_1),
        Return(),
    ]
)
