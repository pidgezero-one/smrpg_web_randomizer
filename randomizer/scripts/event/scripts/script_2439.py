# pylint: disable=C0301

"""E2439_FOREST_SECRET_AREA_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09,
            face_direction=SOUTHEAST,
            x=3,
            y=47,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
