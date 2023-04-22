# pylint: disable=C0301

"""E3845_WORLD_MAP_KERO_SEWERS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        EnterArea(
            room_id=R333_KERO_SEWERS_ENTRANCE,
            face_direction=NORTHEAST,
            x=2,
            y=25,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
