# pylint: disable=C0301

"""E3855_WORLD_MAP_BOOSTER_TOWER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        EnterArea(
            room_id=R202_BOOSTER_TOWER_ENTRANCE,
            face_direction=NORTHEAST,
            x=2,
            y=120,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
