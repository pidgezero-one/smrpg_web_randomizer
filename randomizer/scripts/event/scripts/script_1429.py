# pylint: disable=C0301

"""E1429_SUMMON_JUMPING_GOOMBA_MUSHROOM_WAY_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_5, R204_MUSHROOM_WAY_AREA_02, ["EVENT_1429_ret_4"]
        ),
        JmpIfBitSet(TEMP_7044_4, ["EVENT_1429_ret_4"]),
        SetSyncActionScript(NPC_5, A0540_JUMPING_GOOMBA_MUSHROOM_WAY_2),
        Return(),
        Return(identifier="EVENT_1429_ret_4"),
    ]
)
