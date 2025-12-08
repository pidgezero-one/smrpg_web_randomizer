# pylint: disable=C0301

"""E3178_SEWERS_3RD_WATER_TOOM_PIPE_TO_RAT_LINE_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 11),
        SetVarToConst(Y_COORD_2, 100),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE,
            face_direction=SOUTH,
            x=18,
            y=40,
            z=5,
            run_entrance_event=True),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        Return(),
    ]
)
