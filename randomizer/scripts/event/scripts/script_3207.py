# pylint: disable=C0301

"""E3207_SHIP_EXIT_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
        ClearBit(JOHNNY_POSITION),
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        ExitToWorldMap(area=OW34_SUNKEN_SHIP, bit_6=True, bit_7=True),
        Return(),
    ]
)
