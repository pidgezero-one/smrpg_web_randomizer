# pylint: disable=C0301

"""E0504_PIPE_VAULT_SMALL_COIN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        SetVarToConst(TEMP_702A, 1),
        JmpToEvent(E0279_UNKNOWN),
    ]
)
