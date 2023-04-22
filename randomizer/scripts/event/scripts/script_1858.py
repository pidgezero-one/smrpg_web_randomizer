# pylint: disable=C0301

"""E1858_MOLEVILLE_INN_EXIT_TO_EXTERIOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MINECART_CLEARED, ["EVENT_1858_enter_area_3"]),
        EnterArea(
            room_id=R102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES,
            face_direction=SOUTHWEST,
            x=14,
            y=86,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R108_MOLEVILLE_OUTSIDE,
            face_direction=SOUTHWEST,
            x=14,
            y=86,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_1858_enter_area_3",
        ),
        Return(),
    ]
)
