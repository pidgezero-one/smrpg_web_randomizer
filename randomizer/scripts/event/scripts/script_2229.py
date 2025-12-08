# pylint: disable=C0301

"""E2229_KEEP_DARK_ROOM_SUMMON_GOOMBA_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM,
            ["EVENT_2229_ret_4"]),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_2229_ret_4"]),
        SetSyncActionScript(NPC_1, A1009_KEEP_DARK_ROOM_GOOMBA_RUNS_FROM_CHEST),
        SetBit(TEMP_7043_0),
        Return(identifier="EVENT_2229_ret_4"),
    ]
)
