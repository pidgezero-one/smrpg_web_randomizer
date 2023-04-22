# pylint: disable=C0301

"""E2578_BOOSTER_TOWER_SMALL_SAVE_ROOM_BACK_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM,
            face_direction=NORTHWEST,
            x=11,
            y=125,
            z=5,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
