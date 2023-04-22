# pylint: disable=C0301

"""E1314_TOWER_BOSS_1_HIDES_BEHIND_DOORWAY_IN_LOBBY_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TOWER_LOBBY_MOVEMENT, ["EVENT_1314_ret_3"]),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_1314_ret_3"]),
        SetSyncActionScript(NPC_3, A0517_TOWER_BOSS_1_HIDES_BEHIND_DOORWAY_IN_LOBBY_1),
        Return(identifier="EVENT_1314_ret_3"),
    ]
)
