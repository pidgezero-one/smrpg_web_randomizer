# pylint: disable=C0301

"""E3177_SEWERS_STAIR_ROOM_PIPE_TO_FOUR_RAT_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 16),
        SetVarToConst(Y_COORD_2, 46),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS,
            face_direction=SOUTH,
            x=30,
            y=92,
            z=7,
            run_entrance_event=True),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        Return(),
    ]
)
