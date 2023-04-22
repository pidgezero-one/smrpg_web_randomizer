# pylint: disable=C0301

"""E3777_ROYAL_BUS_PLATFORM_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3777_enter_area_3"]),
        EnterArea(
            room_id=R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA,
            face_direction=SOUTHEAST,
            x=9,
            y=25,
            z=2,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA,
            face_direction=SOUTHEAST,
            x=9,
            y=25,
            z=2,
            run_entrance_event=True,
            identifier="EVENT_3777_enter_area_3",
        ),
        Return(),
    ]
)
