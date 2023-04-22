# pylint: disable=C0301

"""E1426_SUMMON_RIGHT_GOOMBA_IN_MUSHROOM_WAY_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_3, R204_MUSHROOM_WAY_AREA_02, ["EVENT_1426_ret_4"]
        ),
        JmpIfBitSet(TEMP_7044_5, ["EVENT_1426_ret_4"]),
        SetSyncActionScript(NPC_3, A0538_RIGHT_GOOMBA_IN_MUSHROOM_WAY_2),
        Return(),
        Return(identifier="EVENT_1426_ret_4"),
    ]
)
