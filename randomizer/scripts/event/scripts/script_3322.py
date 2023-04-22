# pylint: disable=C0301

"""E3322_VOLCANO_1ST_ROOM_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        ExitToWorldMap(area=OW50_BARREL_VOLCANO, bit_6=True, bit_7=True),
        Return(),
    ]
)
