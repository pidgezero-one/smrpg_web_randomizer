# pylint: disable=C0301

"""E3847_WORLD_MAP_TADPOLE_POND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        EnterArea(
            room_id=R075_TADPOLE_POND_AREA_01,
            face_direction=NORTHEAST,
            x=5,
            y=66,
            z=0,
            run_entrance_event=True),
        Return(),
    ]
)
