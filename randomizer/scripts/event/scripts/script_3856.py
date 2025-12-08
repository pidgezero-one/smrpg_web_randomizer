# pylint: disable=C0301

"""E3856_WORLD_MAP_MARRYMORE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_3856_enter_area_3"]),
        EnterArea(
            room_id=R005_MARRYMORE_OUTSIDE_DURING_BOOSTER,
            face_direction=NORTHWEST,
            x=8,
            y=92,
            z=0,
            run_entrance_event=True),
        Return(),
        EnterArea(
            room_id=R064_MARRYMORE_OUTSIDE,
            face_direction=NORTHWEST,
            x=8,
            y=92,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_3856_enter_area_3"),
        Return(),
    ]
)
