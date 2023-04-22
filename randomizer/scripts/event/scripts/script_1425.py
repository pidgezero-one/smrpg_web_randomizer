# pylint: disable=C0301

"""E1425_SUMMON_LEFT_GOOMBA_IN_MUSHROOM_WAY_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_2, R204_MUSHROOM_WAY_AREA_02, ["EVENT_1425_ret_4"]
        ),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_1425_ret_4"]),
        SetSyncActionScript(NPC_2, A0537_LEFT_GOOMBA_IN_MUSHROOM_WAY_2),
        Return(),
        Return(identifier="EVENT_1425_ret_4"),
    ]
)
