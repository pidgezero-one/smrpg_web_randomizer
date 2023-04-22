# pylint: disable=C0301

"""E2593_ABYSS_PRE_FIRST_BOSS_BOLT"""

from randomizer.scripts.event.script_imports import *

script = EventScript([SetBit(TEMP_7043_0), ClearBit(TEMP_7043_1), Return()])
