# pylint: disable=C0301

"""E1566_LANDS_END_DOG_PIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_3, ["EVENT_1566_ret_10"]),
        SetSyncActionScript(NPC_0, A0818_LANDS_END_CHOW_JUMP_OUT_OF_PIT),
        Pause(9),
        SetSyncActionScript(NPC_1, A0818_LANDS_END_CHOW_JUMP_OUT_OF_PIT),
        Pause(9),
        SetSyncActionScript(NPC_2, A0818_LANDS_END_CHOW_JUMP_OUT_OF_PIT),
        SetBit(TEMP_7043_3),
        Pause(1, identifier="EVENT_1566_pause_7"),
        JmpIfBitClear(TEMP_7044_7, ["EVENT_1566_pause_7"]),
        Pause(2),
        Return(identifier="EVENT_1566_ret_10"),
    ]
)
