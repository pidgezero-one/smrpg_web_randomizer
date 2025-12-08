# pylint: disable=C0301

"""E0423_PIPE_VAULT_PLATFORMING_ROOM_EXIT_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 25),
        SetVarToConst(Y_COORD_2, 100),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R126_PIPE_VAULT_AREA_06_LINE_OF_RED_PIPES,
            face_direction=NORTHEAST,
            x=2,
            y=100,
            z=1,
            run_entrance_event=True),
        JmpToEvent(E0269_PIPE_UP_SUBROUTINE),
    ]
)
