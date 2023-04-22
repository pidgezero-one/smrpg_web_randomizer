# pylint: disable=C0301

"""E1860_MOLEVILLE_SWAP_SHOP_EXIT_TO_EXTERIOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MINECART_CLEARED, ["EVENT_1860_enter_area_3"]),
        EnterArea(
            room_id=R102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES,
            face_direction=SOUTHWEST,
            x=24,
            y=70,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R108_MOLEVILLE_OUTSIDE,
            face_direction=SOUTHWEST,
            x=24,
            y=70,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_1860_enter_area_3",
        ),
        Return(),
    ]
)
