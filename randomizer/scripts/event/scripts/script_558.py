# pylint: disable=C0301

"""E0558_ROSE_TOWN_SHOP_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(FOREST_LIBERATED, ["EVENT_558_enter_area_3"]),
        EnterArea(
            room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE,
            face_direction=SOUTHWEST,
            x=20,
            y=47,
            z=1,
            run_entrance_event=True),
        Return(),
        EnterArea(
            room_id=R084_ROSE_TOWN_OUTSIDE,
            face_direction=SOUTHWEST,
            x=20,
            y=47,
            z=1,
            run_entrance_event=True,
            identifier="EVENT_558_enter_area_3"),
        Return(),
    ]
)
