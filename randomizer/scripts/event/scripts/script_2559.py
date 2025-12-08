# pylint: disable=C0301

"""E2559_BEAN_VALLEY_BEANSTALK_ROOM_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 26),
        SetVarToConst(Y_COORD_2, 22),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R254_BEAN_VALLEY_SMILAX_AREA,
            face_direction=SOUTH,
            x=27,
            y=70,
            z=0,
            run_entrance_event=True),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        Return(),
    ]
)
