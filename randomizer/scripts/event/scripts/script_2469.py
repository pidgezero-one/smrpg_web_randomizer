# pylint: disable=C0301

"""E2469_BEAN_VALLEY_1ST_PROGRESSION_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 9),
        SetVarToConst(Y_COORD_2, 109),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R252_BEAN_VALLEY_MAIN_AREA,
            face_direction=SOUTH,
            x=16,
            y=72,
            z=0,
            run_entrance_event=True,
        ),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        Return(),
    ]
)
