# pylint: disable=C0301

"""E3741_NIMBUS_CASTLE_ANTECHAMBER_EXIT_TO_NOTE_HALLWAY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3741_enter_area_3"]),
        EnterArea(
            room_id=R412_NIMBUS_CASTLE_AREA_11_LONG_HALLWAY_DOOR_TO_KINGS_CELLAR,
            face_direction=SOUTHWEST,
            x=29,
            y=13,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R497_NIMBUS_CASTLE_AREA_06_____DUMMY,
            face_direction=SOUTHWEST,
            x=29,
            y=13,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_3741_enter_area_3",
        ),
        Return(),
    ]
)
