# pylint: disable=C0301

"""E0492_PIPE_VAULT_PIRANHA_TIMER_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [JmpIfBitSet(TEMP_7044_3, ["EVENT_256_ret_0"]), SetBit(TEMP_7044_3), Return()]
)
