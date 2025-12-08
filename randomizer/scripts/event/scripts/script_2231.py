# pylint: disable=C0301

"""E2231_KEEP_DARK_ROOM_SUMMON_GOOMBA_3"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_5,
            R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM,
            ["EVENT_2231_ret_5"]),
        JmpIfBitSet(TEMP_7043_2, ["EVENT_2231_ret_5"]),
        SetSyncActionScript(NPC_5, A1013_KEEP_DARK_ROOM_KAMIKAZE_GOOMBA),
        RemoveObjectFromSpecificLevel(
            NPC_5, R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM
        ),
        SetBit(TEMP_7043_2),
        Return(identifier="EVENT_2231_ret_5"),
    ]
)
