# pylint: disable=C0301

"""E0510_PIPE_VAULT_CROUCH_ROOM_CLEAR_BITS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [JmpIfBitClear(TEMP_7043_1, ["EVENT_256_ret_0"]), ClearBit(TEMP_7043_1), Return()]
)
