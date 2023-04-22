# pylint: disable=C0301

"""E3127_SEWER_EXIT_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        EnterArea(
            room_id=R333_KERO_SEWERS_ENTRANCE, face_direction=SOUTH, x=5, y=20, z=1
        ),
        FadeInFromBlack(sync=True),
        ActionQueueAsync(
            target=MARIO, subscript=[ASJumpToHeight(height=144, silent=True)]
        ),
        Return(),
    ]
)
