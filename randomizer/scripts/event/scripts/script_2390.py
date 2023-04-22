# pylint: disable=C0301

"""E2390_ABYSS_1ST_SAVE_POINT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_7044_4),
        RunEventAsSubroutine(E0080_SAVE_BLOCK_SUBROUTINE),
        ClearBit(TEMP_7044_4),
        Return(),
    ]
)
