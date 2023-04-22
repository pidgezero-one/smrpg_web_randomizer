# pylint: disable=C0301

"""E1315_TOWER_BOSS_1_HIDES_BEHIND_DOORWAY_IN_LOBBY_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TOWER_LOBBY_MOVEMENT, ["EVENT_1315_ret_5"]),
        JmpIfBitClear(TEMP_7043_0, ["EVENT_1315_ret_5"]),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_1315_ret_5"]),
        SetSyncActionScript(NPC_3, A0518_TOWER_BOSS_1_HIDES_BEHIND_DOORWAY_IN_LOBBY_2),
        SetBit(TEMP_7043_1),
        SetBit(TOWER_LOBBY_MOVEMENT),
        Return(identifier="EVENT_1315_ret_5"),
    ]
)
