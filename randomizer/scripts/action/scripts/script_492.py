"""A0492_MUSHROOM_WAY_BOSS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpIfObjectWithinRangeSameZ(
            comparing_npc=MARIO,
            usually=0,
            tiles=6,
            destinations=["ACTION_492_set_bit_3"],
            identifier="ACTION_492_db_0",
        ),
        Pause(1),
        Jmp(["ACTION_492_db_0"]),
        SetBit(TEMP_7044_6, identifier="ACTION_492_set_bit_3"),
        Return(),
    ]
)
