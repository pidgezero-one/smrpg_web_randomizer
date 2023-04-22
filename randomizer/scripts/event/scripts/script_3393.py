# pylint: disable=C0301

"""E3393_SUPER_JUMP_COMPARE_FOR_1ST_PRIZE"""

from randomizer.scripts.event.script_imports import *

script = EventScript([CompareVarToConst(PRIMARY_TEMP_7000, 30), Return()])
