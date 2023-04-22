"""A0677_MUSHROOM_DERBY_UNKNOWN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpIfRandom2of3(
            ["ACTION_677_pause_2", "ACTION_677_pause_3"],
            identifier="ACTION_677_jmp_if_random_above_66_0",
        ),
        Pause(30),
        Pause(30, identifier="ACTION_677_pause_2"),
        Pause(30, identifier="ACTION_677_pause_3"),
        JumpToHeight(height=64, silent=True),
        Pause(1, identifier="ACTION_677_pause_5"),
        JmpIfBitSet(TEMP_7044_7, ["ACTION_677_pause_9"]),
        JmpIfObjectInAir(DUMMY_0X07, ["ACTION_677_pause_5"]),
        Jmp(["ACTION_677_jmp_if_random_above_66_0"]),
        Pause(1, identifier="ACTION_677_pause_9"),
        JmpIfObjectInAir(DUMMY_0X07, ["ACTION_677_pause_9"]),
        FaceNortheast(),
        Return(),
    ]
)
