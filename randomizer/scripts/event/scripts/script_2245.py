# pylint: disable=C0301

"""E2245_SETS_MUSHROOM_BOY_SHOP_STATE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(SEASIDE_BOSS_SET, ["EVENT_2245_jmp_if_bit_set_0"]),
        EnterArea(
            room_id=R216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE,
            face_direction=NORTHEAST,
            x=24,
            y=40,
            z=0,
            run_entrance_event=True),
        Return(),
        JmpIfBitSet(
            SEASIDE_SHED_EMPTIED,
            ["EVENT_2245_enter_area_3"],
            identifier="EVENT_2245_jmp_if_bit_set_0"),
        EnterArea(
            room_id=R312_SEASIDE_TOWN_MUSHROOM_BOYS_SHOP,
            face_direction=NORTHEAST,
            x=24,
            y=40,
            z=0,
            run_entrance_event=True),
        Return(),
        EnterArea(
            room_id=R312_SEASIDE_TOWN_MUSHROOM_BOYS_SHOP,
            face_direction=NORTHEAST,
            x=24,
            y=40,
            z=0,
            show_banner=True,
            run_entrance_event=True,
            identifier="EVENT_2245_enter_area_3"),
        Return(),
    ]
)
