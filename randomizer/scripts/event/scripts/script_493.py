# pylint: disable=C0301

"""E0493_PIPE_VAULT_PIRANHA_BIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [JmpIfBitClear(TEMP_7044_3, ["EVENT_256_ret_0"]), ClearBit(TEMP_7044_3), Return()]
)
