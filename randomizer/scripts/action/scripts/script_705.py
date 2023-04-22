"""A0705_BOOSTER_HILL_LAYER_3"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetVarToRandom(
            PRIMARY_TEMP_700C, 16, identifier="ACTION_705_set_var_to_random_0"
        ),
        AddConstToVar(PRIMARY_TEMP_700C, 15),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(2),
        EndLoop(),
        JmpIfRandom2of3(
            ["ACTION_705_set_animation_speed_14", "ACTION_705_set_animation_speed_19"]
        ),
        Pause(31),
        JmpIfRandom2of3(
            ["ACTION_705_set_animation_speed_14", "ACTION_705_set_animation_speed_19"]
        ),
        SetWalkingSpeed(VERY_FAST),
        JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
        WalkSoutheastSteps(32),
        JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
        Pause(71),
        Jmp(["ACTION_705_set_var_to_random_0"]),
        SetWalkingSpeed(FASTEST, identifier="ACTION_705_set_animation_speed_14"),
        JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
        WalkSouthSteps(16),
        JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
        Pause(41),
        SetWalkingSpeed(VERY_FAST, identifier="ACTION_705_set_animation_speed_19"),
        JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
        WalkNorthwestSteps(32),
        JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
        Pause(71),
        Jmp(["ACTION_705_set_var_to_random_0"]),
        Return(identifier="ACTION_705_ret_25"),
    ]
)
