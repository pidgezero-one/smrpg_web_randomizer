# pylint: disable=C0301

"""E2244_SETS_SEASIDE_HEALTH_STORE_STATE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(SEASIDE_BOSS_SET, ["EVENT_2244_jmp_if_bit_set_0"]),
        EnterArea(
            room_id=R215_SEASIDE_TOWN_DURING_YARIDOVICH_HEALTH_FOOD_STORE_LEFTMOST,
            face_direction=NORTHEAST,
            x=24,
            y=16,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        JmpIfBitSet(
            SEASIDE_SHED_EMPTIED,
            ["EVENT_2244_enter_area_3"],
            identifier="EVENT_2244_jmp_if_bit_set_0",
        ),
        EnterArea(
            room_id=R311_SEASIDE_TOWN_HEALTH_FOOD_STORE,
            face_direction=NORTHEAST,
            x=24,
            y=16,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R311_SEASIDE_TOWN_HEALTH_FOOD_STORE,
            face_direction=NORTHEAST,
            x=24,
            y=16,
            z=0,
            show_banner=True,
            run_entrance_event=True,
            identifier="EVENT_2244_enter_area_3",
        ),
        Return(),
    ]
)
