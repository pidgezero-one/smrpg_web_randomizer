# pylint: disable=C0301

"""E3844_WORLD_MAP_BANDITS_WAY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        EnterArea(
            room_id=R076_BANDITS_WAY_AREA_01,
            face_direction=SOUTHEAST,
            x=2,
            y=7,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
