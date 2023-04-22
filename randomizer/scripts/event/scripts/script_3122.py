# pylint: disable=C0301

"""E3122_SEWER_BOSS_ROOM_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        EnterArea(
            room_id=R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS,
            face_direction=SOUTH,
            x=12,
            y=108,
            z=11,
        ),
        RunEventAsSubroutine(E0014_STANDARD_ROOM_LOADER),
        ActionQueueAsync(
            target=MARIO, subscript=[ASJumpToHeight(height=144, silent=True)]
        ),
        Return(),
    ]
)
