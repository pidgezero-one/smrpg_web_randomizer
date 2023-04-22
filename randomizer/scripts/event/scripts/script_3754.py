# pylint: disable=C0301

"""E3754_HOT_SPRINGS_FALL_TO_VOLCANO"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutToBlack(sync=False),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BARREL_VOLCANO),
        SetBit(MAP_BARREL_VOLCANO),
        JmpToEvent(E3321_VOLCANO_ENTER_1ST_ROOM),
        Return(),
    ]
)
