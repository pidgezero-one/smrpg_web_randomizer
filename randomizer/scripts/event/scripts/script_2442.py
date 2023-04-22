# pylint: disable=C0301

"""E2442_FOREST_INITIATE_MAZE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09,
            face_direction=NORTHEAST,
            x=3,
            y=61,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
