# pylint: disable=C0301

"""E3851_WORLD_MAP_FOREST_MAZE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        EnterArea(
            room_id=R224_FOREST_MAZE_AREA_01,
            face_direction=NORTHWEST,
            x=7,
            y=23,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
