# pylint: disable=C0301

"""E1903_ABYSS_SIDE_TREASURE_ROOMS_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(ABYSS_TWO_CHEST_ROOM_DIRECTIONAL_BIT, ["EVENT_1903_enter_area_3"]),
        EnterArea(
            room_id=R445_SMITHY_FACTORY_AREA_10_FALL_FROM_AREA_09,
            face_direction=SOUTHWEST,
            x=7,
            y=21,
            z=0,
            run_entrance_event=True),
        Return(),
        EnterArea(
            room_id=R474_SMITHY_FACTORY_AREA_15_FALLING_YARIDOVICHS,
            face_direction=SOUTHWEST,
            x=20,
            y=21,
            z=8,
            run_entrance_event=True,
            identifier="EVENT_1903_enter_area_3"),
        Return(),
    ]
)
