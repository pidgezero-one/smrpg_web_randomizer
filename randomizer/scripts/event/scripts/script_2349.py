# pylint: disable=C0301

"""E2349_TOWER_SPOOKUM_JUMPS_OUT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInCurrentLevel(NPC_5, ["EVENT_2349_ret_4"]),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_2349_ret_4"]),
        SetBit(TEMP_7043_0),
        SetSyncActionScript(NPC_5, A0387_JUMPING_TOWER_SPOOKUM),
        Return(identifier="EVENT_2349_ret_4"),
    ]
)
