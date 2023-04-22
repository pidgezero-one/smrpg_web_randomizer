# pylint: disable=C0301

"""E3671_NIMBUS_CASTLE_FIRST_POST_THRONE_HALL_EXIT_TO_THRONE_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3671_enter_area_3"]),
        EnterArea(
            room_id=R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA,
            face_direction=SOUTHEAST,
            x=8,
            y=47,
            z=2,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA,
            face_direction=SOUTHEAST,
            x=8,
            y=47,
            z=2,
            run_entrance_event=True,
            identifier="EVENT_3671_enter_area_3",
        ),
        Return(),
    ]
)
