# pylint: disable=C0301

"""E3663_NIMBUS_CASTLE_LEFT_SHAMAN_ROOM_EXIT_TO_5_DOOR_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3663_enter_area_3"]),
        EnterArea(
            room_id=R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            face_direction=SOUTHWEST,
            x=23,
            y=103,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            face_direction=SOUTHWEST,
            x=23,
            y=103,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_3663_enter_area_3",
        ),
        Return(),
    ]
)
