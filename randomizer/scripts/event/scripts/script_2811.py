# pylint: disable=C0301

"""E2811_MUSHROOM_WAY_3_LOWER_QUICK_SPINY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_2, ["EVENT_2811_ret_2"]),
        SetSyncActionScript(NPC_4, A0494_FAST_SPINY),
        Return(identifier="EVENT_2811_ret_2"),
    ]
)
