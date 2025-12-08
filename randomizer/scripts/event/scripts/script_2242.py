# pylint: disable=C0301

"""E2242_SETS_SEASIDE_WPN_ARM_SHOP_STATE_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(SEASIDE_BOSS_SET, ["EVENT_2242_jmp_if_bit_set_0"]),
        EnterArea(
            room_id=R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP,
            face_direction=NORTHWEST,
            x=15,
            y=72,
            z=0,
            run_entrance_event=True),
        Return(),
        JmpIfBitSet(
            SEASIDE_SHED_EMPTIED,
            ["EVENT_2242_enter_area_3"],
            identifier="EVENT_2242_jmp_if_bit_set_0"),
        EnterArea(
            room_id=R310_SEASIDE_TOWN_WEAPON_AND_ARMOR_SHOP,
            face_direction=NORTHWEST,
            x=15,
            y=72,
            z=0,
            run_entrance_event=True),
        Return(),
        EnterArea(
            room_id=R310_SEASIDE_TOWN_WEAPON_AND_ARMOR_SHOP,
            face_direction=NORTHWEST,
            x=15,
            y=72,
            z=0,
            show_banner=True,
            run_entrance_event=True,
            identifier="EVENT_2242_enter_area_3"),
        Return(),
    ]
)
