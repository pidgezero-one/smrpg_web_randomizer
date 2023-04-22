# pylint: disable=C0301

"""E0490_RED_ROOM_PIRANHA_3"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [JmpIfBitClear(TEMP_7044_5, ["EVENT_256_ret_0"]), ClearBit(TEMP_7044_5), Return()]
)
