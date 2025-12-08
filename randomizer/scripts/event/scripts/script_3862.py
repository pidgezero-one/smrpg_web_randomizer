# pylint: disable=C0301

"""E3862_WORLD_MAP_MONTRO_TOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        EnterArea(
            room_id=R267_MONSTRO_TOWN_ENTRANCE,
            face_direction=SOUTHWEST,
            x=10,
            y=101,
            z=0,
            run_entrance_event=True),
        Return(),
    ]
)
