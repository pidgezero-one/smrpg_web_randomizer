# pylint: disable=C0301

"""E3515_NIMBUS_CASTLE_EGG_ROOM_EXIT_TO_NEXT_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3515_enter_area_1"]),
        EnterArea(
            room_id=R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
            face_direction=NORTHEAST,
            x=10,
            y=107,
            z=3,
            run_entrance_event=True),
        Return(),
        EnterArea(
            room_id=R498_NIMBUS_CASTLE_AREA_10_____DUMMY,
            face_direction=NORTHEAST,
            x=10,
            y=107,
            z=3,
            run_entrance_event=True,
            identifier="EVENT_3515_enter_area_1"),
        Return(),
    ]
)
