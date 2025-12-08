# pylint: disable=C0301

"""E3922_TEMPLE_SET_SIGNAL_RING_DIRECTIONAL_BIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        EnterArea(
            room_id=R428_BELOME_TEMPLE_AREA_01_WWARP_TRAMPOLINE,
            face_direction=NORTHEAST,
            x=16,
            y=117,
            z=4,
            run_entrance_event=True),
        Return(),
    ]
)
