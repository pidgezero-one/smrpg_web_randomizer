# pylint: disable=C0301

"""E3767_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_EXIT_TO_4_PATH_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3767_enter_area_3"]),
        EnterArea(
            room_id=R115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA,
            face_direction=SOUTHWEST,
            x=29,
            y=13,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA,
            face_direction=SOUTHWEST,
            x=29,
            y=13,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_3767_enter_area_3",
        ),
        Return(),
    ]
)
