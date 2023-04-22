# pylint: disable=C0301

"""E3666_NIMBUS_CASTLE_NOTE_HALLWAY_EXIT_TO_TWO_LEVEL_CHEST_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3666_enter_area_3"]),
        EnterArea(
            room_id=R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
            face_direction=SOUTHWEST,
            x=14,
            y=103,
            z=3,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R498_NIMBUS_CASTLE_AREA_10_____DUMMY,
            face_direction=SOUTHWEST,
            x=14,
            y=103,
            z=3,
            run_entrance_event=True,
            identifier="EVENT_3666_enter_area_3",
        ),
        Return(),
    ]
)
