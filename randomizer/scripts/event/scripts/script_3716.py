# pylint: disable=C0301

"""E3716_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_RIGHT_FAN_GUST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1),
        JmpIfBitSet(TEMP_7043_6, ["EVENT_3716_set_bit_3"]),
        JmpToEvent(E3716_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_RIGHT_FAN_GUST),
        SetBit(TEMP_7043_4, identifier="EVENT_3716_set_bit_3"),
        Pause(1, identifier="EVENT_3716_pause_4"),
        JmpIfBitClear(TEMP_7043_6, ["EVENT_3716_set_action_script_sync_7"]),
        Jmp(["EVENT_3716_pause_4"]),
        SetSyncActionScript(
            MARIO,
            A0814_MARIO_BLOWN_BY_FAN,
            identifier="EVENT_3716_set_action_script_sync_7"),
        ClearBit(TEMP_7043_4),
        ClearBit(TEMP_7043_5),
        JmpToEvent(E3716_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_RIGHT_FAN_GUST),
    ]
)
