# pylint: disable=C0301

"""E0754_MUSHROOM_KINGDOM_SHOP_BASEMENT_STAIRWAY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(MUSHROOM_KINGDOM_OCCUPIED, ["EVENT_754_enter_area_6"]),
        JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_754_enter_area_8"]),
        EnterArea(
            room_id=R491_MUSHROOM_KINGDOM_ITEM_SHOP_TOP_FLOOR,
            face_direction=NORTHWEST,
            x=20,
            y=23,
            z=1,
            z_add_half_unit=True,
            run_entrance_event=True,
            identifier="EVENT_754_enter_area_6"),
        Return(),
        EnterArea(
            room_id=R483_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_TOP_FLOOR,
            face_direction=NORTHWEST,
            x=20,
            y=23,
            z=1,
            z_add_half_unit=True,
            run_entrance_event=True,
            identifier="EVENT_754_enter_area_8"),
        Return(),
    ]
)
