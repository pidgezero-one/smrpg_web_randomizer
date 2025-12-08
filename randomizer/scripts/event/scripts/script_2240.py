# pylint: disable=C0301

"""E2240_SETS_SEASIDE_INN_STATE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(SEASIDE_BOSS_SET, ["EVENT_2240_jmp_if_bit_set_0"]),
        EnterArea(
            room_id=R209_SEASIDE_TOWN_DURING_YARIDOVICH_INN_1F,
            face_direction=NORTHEAST,
            x=4,
            y=49,
            z=0,
            run_entrance_event=True),
        Return(),
        JmpIfBitSet(
            SEASIDE_SHED_EMPTIED,
            ["EVENT_2240_enter_area_3"],
            identifier="EVENT_2240_jmp_if_bit_set_0"),
        EnterArea(
            room_id=R305_SEASIDE_TOWN_INN_1F,
            face_direction=NORTHEAST,
            x=4,
            y=49,
            z=0,
            run_entrance_event=True),
        Return(),
        EnterArea(
            room_id=R305_SEASIDE_TOWN_INN_1F,
            face_direction=NORTHEAST,
            x=4,
            y=49,
            z=0,
            show_banner=True,
            run_entrance_event=True,
            identifier="EVENT_2240_enter_area_3"),
        Return(),
    ]
)
