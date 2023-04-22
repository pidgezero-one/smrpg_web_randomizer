# pylint: disable=C0301

"""E3324_VOLCANO_3_LIFT_ROOM_DONUT_LIFT"""

from randomizer.scripts.event.script_imports import *

script = EventScript([SetSyncActionScript(MEM_70A8, A0930_DONUT_LIFT_FALL), Return()])
