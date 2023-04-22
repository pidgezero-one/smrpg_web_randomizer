# pylint: disable=C0301

"""E2331_BOOSTER_PASS_2ND_ROOM_SPINY_SUMMONER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInCurrentLevel(NPC_3, ["EVENT_2331_ret_4"]),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_2331_ret_4"]),
        SetBit(TEMP_7043_3),
        SetSyncActionScript(NPC_3, A0692_BOOSTER_PASS_SPINY),
        Return(identifier="EVENT_2331_ret_4"),
    ]
)
