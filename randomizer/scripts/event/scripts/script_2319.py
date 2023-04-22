# pylint: disable=C0301

"""E2319_BOOSTER_PASS_2ND_ROOM_SPINY_SUMMONER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInCurrentLevel(NPC_0, ["EVENT_2319_ret_4"]),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_2319_ret_4"]),
        SetBit(TEMP_7043_0),
        SetSyncActionScript(NPC_0, A0692_BOOSTER_PASS_SPINY),
        Return(identifier="EVENT_2319_ret_4"),
    ]
)
