# pylint: disable=C0301

"""E2241_SETS_SEASIDE_ELDERS_HOUSE_STATE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(SEASIDE_BOSS_SET, ["EVENT_2241_enter_area_1"]),
        EnterArea(
            room_id=R211_SEASIDE_TOWN_DURING_YARIDOVICH_ELDERS_HOUSE_1F,
            face_direction=NORTHEAST,
            x=3,
            y=101,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R307_SEASIDE_TOWN_ELDERS_HOUSE_1F,
            face_direction=NORTHEAST,
            x=3,
            y=101,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_2241_enter_area_1",
        ),
        Return(),
    ]
)
