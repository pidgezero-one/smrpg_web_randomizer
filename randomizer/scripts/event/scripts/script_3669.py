# pylint: disable=C0301

"""E3669_NIMBUS_CASTLE_SOLO_BIRD_STATUE_ROOM_EXIT_TO_5_DOOR_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3669_enter_area_3"]),
        EnterArea(
            room_id=R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            face_direction=NORTHEAST,
            x=26,
            y=123,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            face_direction=NORTHEAST,
            x=26,
            y=123,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_3669_enter_area_3",
        ),
        Return(),
    ]
)
