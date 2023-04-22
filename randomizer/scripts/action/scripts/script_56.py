"""A0056_SEWER_WATER_DRAIN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToCurrentLevel(identifier="ACTION_56_set_700C_to_current_level_0"),
        Pause(1),
        JmpIfBitClear(SEWER_WATER_LEVEL, ["ACTION_56_set_700C_to_current_level_0"]),
        SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
        SetSpriteSequence(index=1, is_sequence=True, looping=False),
        ClearSolidityBits(cant_walk_through=True, bit_7=True),
        Return(),
    ]
)
