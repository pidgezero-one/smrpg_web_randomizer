# pylint: disable=C0301

"""E3296_SEA_ENTRANCE_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        ExitToWorldMap(area=OW33_SEA, bit_6=True, bit_7=True),
        Return(),
    ]
)
