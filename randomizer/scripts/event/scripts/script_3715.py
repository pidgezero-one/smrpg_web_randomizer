# pylint: disable=C0301

"""E3715_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_RIGHT_FAN_GUST_PATH"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7043_4, ["EVENT_3584_ret_0"]),
        JmpIfBitSet(TEMP_7043_5, ["EVENT_3584_ret_0"]),
        SetSyncActionScript(MARIO, A0809_MARIO_BLOWN_BY_FAN),
        SetBit(TEMP_7043_5),
        Return(),
    ]
)
