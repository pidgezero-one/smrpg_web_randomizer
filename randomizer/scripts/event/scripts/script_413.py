# pylint: disable=C0301

"""E0413_CLEAR_TEMP_7044_0"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [JmpIfBitClear(TEMP_7044_0, ["EVENT_256_ret_0"]), ClearBit(TEMP_7044_0), Return()]
)
