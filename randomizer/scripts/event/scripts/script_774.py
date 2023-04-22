# pylint: disable=C0301

"""E0774_FOREST_MAZE_BOSS_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0775_FOREST_MAZE_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER),
    ]
)
