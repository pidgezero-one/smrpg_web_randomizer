# pylint: disable=C0301

"""E3857_WORLD_MAP_STAR_HILL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R145_STAR_HILL_AREA_01,
            face_direction=NORTHWEST,
            x=8,
            y=37,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
