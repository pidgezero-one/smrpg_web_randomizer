# pylint: disable=C0301

"""E3510_BOOSTER_HILL_EXIT_TO_WORLD_MAP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(MAP_BOOSTER_HILL),
        ExitToWorldMap(area=OW27_BOOSTER_HILL, bit_6=True, bit_7=True),
        Return(),
    ]
)
