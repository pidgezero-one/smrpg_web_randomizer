"""A0704_BOOSTER_HILL_LAYER_1"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetAllSpeeds(FAST),
        Walk1StepNorthwest(identifier="ACTION_704_walk_1_step_northwest_1"),
        Jmp(["ACTION_704_walk_1_step_northwest_1"]),
        Return(),
    ]
)
