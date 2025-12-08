# pylint: disable=C0301

"""E2547_BEAN_VALLEY_RIGHTMOST_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 16),
        SetVarToConst(Y_COORD_2, 23),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM,
            face_direction=SOUTH,
            x=4,
            y=106,
            z=7,
            run_entrance_event=True),
        Return(),
    ]
)
