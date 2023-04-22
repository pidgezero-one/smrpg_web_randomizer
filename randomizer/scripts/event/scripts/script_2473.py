# pylint: disable=C0301

"""E2473_BEAN_VALLEY_PIPE_TO_1ST_CHEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 5),
        SetVarToConst(Y_COORD_2, 87),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R252_BEAN_VALLEY_MAIN_AREA,
            face_direction=SOUTH,
            x=13,
            y=95,
            z=0,
            run_entrance_event=True,
        ),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        Return(),
    ]
)
