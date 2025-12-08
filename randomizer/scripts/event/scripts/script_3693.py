# pylint: disable=C0301

"""E3693_NIMBUS_INN_EXIT_TO_EXTERIOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_7042_4),
        ClearBit(TEMP_7042_5),
        ClearBit(TEMP_7042_6),
        ClearBit(TEMP_7042_7),
        ClearBit(TEMP_7042_3),
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3693_enter_area_8"]),
        EnterArea(
            room_id=R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA,
            face_direction=SOUTHWEST,
            x=4,
            y=48,
            z=2,
            run_entrance_event=True),
        Return(),
        EnterArea(
            room_id=R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA,
            face_direction=SOUTHWEST,
            x=4,
            y=48,
            z=2,
            run_entrance_event=True,
            identifier="EVENT_3693_enter_area_8"),
        Return(),
    ]
)
