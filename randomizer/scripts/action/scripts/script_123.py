"""A0123_MK_BRANCH_HALLWAY_HENCHMAN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpIfRandom1of2(
            ["ACTION_123_jmp_to_subroutine_4"],
            identifier="ACTION_123_jmp_if_random_above_128_0"),
        JmpToSubroutine(["ACTION_106_set_animation_speed_0"]),
        JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
        Jmp(["ACTION_123_jmp_if_random_above_128_0"]),
        JmpToSubroutine(
            ["ACTION_105_set_animation_speed_0"],
            identifier="ACTION_123_jmp_to_subroutine_4"),
        JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
        Jmp(["ACTION_123_jmp_if_random_above_128_0"]),
    ]
)
