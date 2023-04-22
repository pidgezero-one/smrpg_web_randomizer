"""A0656_RUNNING_YELLOW_YOSHI"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetObjectMemoryBits(
            arg_1=0x0B, bits=[1], identifier="ACTION_656_set_object_memory_bits_0"
        ),
        SetSolidityBits(cant_walk_through=True),
        SetSolidityBits(bit_4=True),
        SetVarToConst(TEMP_702A, 7),
        SetVarToConst(ROSE_WAY_703A, 20),
        SetSequenceSpeed(FAST, identifier="ACTION_656_set_animation_speed_5"),
        SetWalkingSpeed(VERY_SLOW),
        Walk1StepNortheast(),
        JmpToSubroutine(["ACTION_656_dec_short_29"]),
        JmpIfVarEqualsConst(ROSE_WAY_703A, 0, ["ACTION_656_set_animation_speed_21"]),
        JmpIfRandom2of3(
            [
                "ACTION_656_set_animation_speed_5",
                "ACTION_656_jmp_if_var_equals_const_12",
            ]
        ),
        Jmp(["ACTION_656_set_animation_speed_5"]),
        JmpIfVarEqualsConst(
            TEMP_702A,
            0,
            ["ACTION_656_set_animation_speed_5"],
            identifier="ACTION_656_jmp_if_var_equals_const_12",
        ),
        SetSequenceSpeed(VERY_FAST),
        SetWalkingSpeed(SLOW),
        Walk1StepNortheast(),
        JmpToSubroutine(["ACTION_656_dec_short_29"]),
        JmpIfVarEqualsConst(ROSE_WAY_703A, 0, ["ACTION_656_set_animation_speed_21"]),
        JmpToSubroutine(["ACTION_656_dec_short_31"]),
        JmpIfRandom2of3(
            [
                "ACTION_656_jmp_if_var_equals_const_12",
                "ACTION_656_set_animation_speed_5",
            ]
        ),
        Jmp(["ACTION_656_jmp_if_var_equals_const_12"]),
        SetSequenceSpeed(NORMAL, identifier="ACTION_656_set_animation_speed_21"),
        FaceSouthwest(),
        Pause(60),
        SetWalkingSpeed(SLOW),
        WalkSouthwestSteps(20),
        FaceNortheast(),
        Pause(60),
        Jmp(["ACTION_656_set_object_memory_bits_0"]),
        Dec(ROSE_WAY_703A, identifier="ACTION_656_dec_short_29"),
        Return(),
        Dec(TEMP_702A, identifier="ACTION_656_dec_short_31"),
        Return(),
    ]
)
