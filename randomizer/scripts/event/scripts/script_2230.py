# pylint: disable=C0301

"""E2230_KEEP_DARK_ROOM_SUMMON_GOOMBA_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_4,
            R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM,
            ["EVENT_2230_ret_4"],
        ),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_2230_ret_4"]),
        SetSyncActionScript(NPC_4, A1011_KEEP_DARK_ROOM_JUMPING_GOOMBA),
        SetBit(TEMP_7043_1),
        Return(identifier="EVENT_2230_ret_4"),
    ]
)
