# pylint: disable=C0301

"""E3339_VOLCANO_2ND_BOSS_PATH_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER), Return()])
