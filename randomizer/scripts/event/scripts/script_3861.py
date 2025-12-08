# pylint: disable=C0301

"""E3861_WORLD_MAP_LANDS_END"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        EnterArea(
            room_id=R137_LANDS_END_AREA_01,
            face_direction=NORTHEAST,
            x=2,
            y=37,
            z=0,
            run_entrance_event=True),
        Return(),
    ]
)
