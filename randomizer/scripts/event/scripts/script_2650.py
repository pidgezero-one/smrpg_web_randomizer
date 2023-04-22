# pylint: disable=C0301

"""E2650_CASINO_GRATE_GUY_CHECK_IF_SIDEQUEST_COMPLETED"""

from randomizer.scripts.event.script_imports import *

script = EventScript([CompareVarToConst(PRIMARY_TEMP_7000, 100), Return()])
