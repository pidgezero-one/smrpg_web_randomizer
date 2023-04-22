# pylint: disable=C0301

"""E2425_FOREST_MAZE_SECRET_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(FOREST_MAZE_SECRET_FOUND),
        ClearBit(DIRECTIONAL_7047_1),
        Jmp(["EVENT_2418_play_sound_63"]),
    ]
)
