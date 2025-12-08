# pylint: disable=C0301

"""E3868_WORLD_MAP_BOWSERS_KEEP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        RunEventAsSubroutine(E3375_KEEP_SET_DOOR_ORDER),
        EnterArea(
            room_id=R476_BOWSERS_KEEP_2ND_TIME_AREA_01,
            face_direction=NORTHEAST,
            x=4,
            y=37,
            z=0,
            run_entrance_event=True),
        Return(),
    ]
)
