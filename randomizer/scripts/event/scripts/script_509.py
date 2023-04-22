# pylint: disable=C0301

"""E0509_PIPE_VAULT_CROUCH_ITEM_RESET"""

from randomizer.scripts.event.script_imports import *

script = EventScript([ClearBit(TEMP_7043_0), Return()])
