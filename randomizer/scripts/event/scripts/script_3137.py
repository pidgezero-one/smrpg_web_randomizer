# pylint: disable=C0301

"""E3137_SEWERS_1ST_WATER_ROOM_PIPE_TO_TUTORIAL_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 12),
        SetVarToConst(Y_COORD_2, 26),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R062_KERO_SEWERS_AREA_01_WATER_ROOM_WSAVE,
            face_direction=SOUTH,
            x=14,
            y=90,
            z=4,
            run_entrance_event=True,
        ),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        Return(),
    ]
)
