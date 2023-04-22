# pylint: disable=C0301

"""E0599_MINES_BOSS_ROOM_ENTRANCE_REVERSE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS,
            face_direction=SOUTHWEST,
            x=26,
            y=97,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
