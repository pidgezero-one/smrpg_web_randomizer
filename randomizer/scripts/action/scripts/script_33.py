"""A0033_FIRST_WIGGLER_BEHIND_STUMP"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceNortheast(),
        JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
        SetPriority(2),
        Walk1StepNortheast(),
        WalkSoutheastSteps(2),
        SetPriority(3),
        JmpIfBitSet(TEMP_7043_7, ["ACTION_33_shift_southwest_steps_11"]),
        WalkSouthwestSteps(5),
        SetPriority(2),
        WalkNorthwestSteps(4),
        Jmp(["ACTION_33_set_priority_18"]),
        WalkSouthwestSteps(3, identifier="ACTION_33_shift_southwest_steps_11"),
        Walk1StepNorthwest(),
        Walk1StepSouthwest(),
        Walk1StepNorthwest(),
        Walk1StepSouthwest(),
        SetPriority(2),
        WalkNorthwestSteps(2),
        SetPriority(3, identifier="ACTION_33_set_priority_18"),
        WalkNortheastSteps(3),
        SetPriority(2),
        JmpIfBitSet(TEMP_7044_0, ["ACTION_33_walk_1_step_northeast_24"]),
        Walk1StepSoutheast(),
        Jmp(["ACTION_32_shift_z_up_steps_20"]),
        Walk1StepNortheast(identifier="ACTION_33_walk_1_step_northeast_24"),
        Walk1StepSoutheast(),
        Walk1StepNortheast(),
        Walk1StepSoutheast(),
        FaceSouthwest(),
        Jmp(["ACTION_32_walk_1_step_f_direction_33"]),
    ]
)
