# pylint: disable=C0301

"""E1681_TEMPLE_TRAMPOLINE_IN_FORTUNE_RESULT_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        EnterArea(
            room_id=R424_BELOME_TEMPLE_AREA_03_PIPE_TO_ROOM_DETERMINED_BY_FORTUNE,
            face_direction=SOUTH,
            x=20,
            y=74,
            z=0),
        Jmp(["EVENT_1690_fade_in_from_black_sync_2"]),
    ]
)
