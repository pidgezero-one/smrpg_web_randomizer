# pylint: disable=C0301

"""E3662_NIMBUS_CASTLE_LEFT_FAN_ROOM_EXIT_TO_BRIDGE_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3662_enter_area_3"]),
        EnterArea(
            room_id=R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE,
            face_direction=NORTHEAST,
            x=1,
            y=121,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R500_NIMBUS_CASTLE_AREA_04_____DUMMY,
            face_direction=NORTHEAST,
            x=1,
            y=121,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_3662_enter_area_3",
        ),
        Return(),
    ]
)
