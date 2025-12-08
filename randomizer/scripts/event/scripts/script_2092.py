# pylint: disable=C0301

"""E2092_MONSTRO_TOWN_BACK_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_708C_4, ["EVENT_2092_open_location_3"]),
        ExitToWorldMap(area=OW38_MONSTRO_TOWN, bit_6=True, bit_7=True),
        Return(),
        ExitToWorldMap(
            area=OW44_MONSTRO_TOWN,
            bit_6=True,
            bit_7=True,
            identifier="EVENT_2092_open_location_3"),
        Return(),
    ]
)
