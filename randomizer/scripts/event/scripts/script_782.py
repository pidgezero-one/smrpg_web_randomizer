# pylint: disable=C0301

"""E0782_MINES_ROOM_THAT_SPLITS_TO_PA_MOLE_PATH_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0783_MINES_ROOM_THAT_SPLITS_TO_PA_MOLE_PATH_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER),
    ]
)
