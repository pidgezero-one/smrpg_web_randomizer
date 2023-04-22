# pylint: disable=C0301

"""E2146_KEEP_DONUT_LIFT"""

from randomizer.scripts.event.script_imports import *

script = EventScript([SetSyncActionScript(MEM_70A8, A0930_DONUT_LIFT_FALL), Return()])
