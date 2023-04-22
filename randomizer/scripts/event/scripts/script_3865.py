# pylint: disable=C0301

"""E3865_WORLD_MAP_BARREL_VOLCANO"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [SetBit(SIGNAL_RING_DIRECTIONAL_BIT), JmpToEvent(E3321_VOLCANO_ENTER_1ST_ROOM)]
)
