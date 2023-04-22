# pylint: disable=C0301

"""E2801_BEAN_VALLEY_EXIT_TO_CASINO"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(MAP_CASINO),
        SetBit(MAP_DIRECTIONAL_BEAN_VALLEY_CASINO),
        JmpIfBitSet(TEMP_708C_4, ["EVENT_2801_open_location_5"]),
        ExitToWorldMap(area=OW39_BEAN_VALLEY, bit_6=True, bit_7=True),
        Return(),
        ExitToWorldMap(
            area=OW45_BEAN_VALLEY,
            bit_6=True,
            bit_7=True,
            identifier="EVENT_2801_open_location_5",
        ),
        Return(),
    ]
)
