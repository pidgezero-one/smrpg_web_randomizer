# pylint: disable=C0301

"""E1972_CLONE_RESERVED"""

from randomizer.scripts.event.script_imports import *

script = EventScript([SetVarToRandom(PRIMARY_TEMP_7000, 10000), Return()])
