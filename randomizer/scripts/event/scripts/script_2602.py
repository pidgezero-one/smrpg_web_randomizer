# pylint: disable=C0301

"""E2602_BEAN_VALLEY_EXIT_TO_WORLD_MAP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_708C_4, ["EVENT_2602_open_location_3"]),
        ExitToWorldMap(area=OW39_BEAN_VALLEY, bit_6=True, bit_7=True),
        Return(),
        ExitToWorldMap(
            area=OW45_BEAN_VALLEY,
            bit_6=True,
            bit_7=True,
            identifier="EVENT_2602_open_location_3",
        ),
        Return(),
    ]
)
