# pylint: disable=C0301

"""E3665_NIMBUS_CASTLE_RIGHT_SHAMAN_ROOM_EXIT_TO_TWO_LEVEL_CHEST_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3665_enter_area_3"]),
        EnterArea(
            room_id=R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
            face_direction=NORTHEAST,
            x=13,
            y=113,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R498_NIMBUS_CASTLE_AREA_10_____DUMMY,
            face_direction=NORTHEAST,
            x=13,
            y=113,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_3665_enter_area_3",
        ),
        Return(),
    ]
)
