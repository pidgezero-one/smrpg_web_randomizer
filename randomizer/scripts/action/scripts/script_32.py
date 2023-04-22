"""A0032_FIRST_WIGGLER_IN_FRONT_OF_STUMP"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceSoutheast(),
        JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
        SetPriority(3),
        Walk1StepSoutheast(),
        WalkNortheastSteps(2),
        SetPriority(2),
        JmpIfBitSet(TEMP_7043_7, ["ACTION_32_shift_northwest_steps_10"]),
        WalkNorthwestSteps(4),
        WalkSouthwestSteps(5),
        Jmp(["ACTION_32_shift_southeast_steps_16"]),
        WalkNorthwestSteps(2, identifier="ACTION_32_shift_northwest_steps_10"),
        Walk1StepSouthwest(),
        Walk1StepNorthwest(),
        Walk1StepSouthwest(),
        Walk1StepNorthwest(),
        WalkSouthwestSteps(3),
        WalkSoutheastSteps(2, identifier="ACTION_32_shift_southeast_steps_16"),
        SetPriority(3),
        JmpIfBitSet(TEMP_7044_0, ["ACTION_32_walk_1_step_northeast_27"]),
        WalkNortheastSteps(2),
        ShiftZUpSteps(2, identifier="ACTION_32_shift_z_up_steps_20"),
        SetPriority(3),
        Walk1StepFDirection(),
        ClearSolidityBits(bit_4=True, cant_walk_through=True),
        DecZCoord1Step(),
        VisibilityOff(),
        Return(),
        Walk1StepNortheast(identifier="ACTION_32_walk_1_step_northeast_27"),
        Walk1StepSoutheast(),
        Walk1StepNortheast(),
        Walk1StepSoutheast(),
        Walk1StepNortheast(),
        FaceNorthwest(),
        Walk1StepFDirection(identifier="ACTION_32_walk_1_step_f_direction_33"),
        Jmp(["ACTION_32_shift_z_up_steps_20"]),
    ]
)
