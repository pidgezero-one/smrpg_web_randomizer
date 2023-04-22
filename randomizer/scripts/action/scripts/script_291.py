"""A0291_MINES_FINAL_BOSS_ROOM_HENCHMAN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(SLOW, identifier="ACTION_291_set_animation_speed_0"),
        SetSequenceSpeed(FAST),
        SetPriority(2),
        WalkNorthwestSteps(2),
        JmpIfRandom2of3(["ACTION_291_set_priority_6", "ACTION_291_set_priority_6"]),
        JmpToSubroutine(["ACTION_293_object_memory_modify_bits_0"]),
        SetPriority(3, identifier="ACTION_291_set_priority_6"),
        WalkNortheastSteps(2),
        JmpIfRandom2of3(["ACTION_291_set_priority_10", "ACTION_291_set_priority_10"]),
        JmpToSubroutine(["ACTION_293_object_memory_modify_bits_0"]),
        SetPriority(3, identifier="ACTION_291_set_priority_10"),
        WalkSoutheastSteps(2),
        JmpIfRandom2of3(["ACTION_291_set_priority_14", "ACTION_291_set_priority_14"]),
        JmpToSubroutine(["ACTION_293_object_memory_modify_bits_0"]),
        SetPriority(2, identifier="ACTION_291_set_priority_14"),
        WalkSouthwestSteps(2),
        JmpIfRandom2of3(
            ["ACTION_291_set_animation_speed_0", "ACTION_291_set_animation_speed_0"]
        ),
        JmpToSubroutine(["ACTION_293_object_memory_modify_bits_0"]),
        Jmp(["ACTION_291_set_animation_speed_0"]),
    ]
)
