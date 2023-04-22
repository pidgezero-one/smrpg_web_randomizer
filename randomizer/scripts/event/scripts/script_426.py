# pylint: disable=C0301

"""E0426_PIPE_VAULT_CHOMPWEED_ROOM_ENTRANCE_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 12),
        SetVarToConst(Y_COORD_2, 84),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R126_PIPE_VAULT_AREA_06_LINE_OF_RED_PIPES,
            face_direction=SOUTHWEST,
            x=7,
            y=90,
            z=1,
            run_entrance_event=True,
        ),
        JmpToEvent(E0269_PIPE_UP_SUBROUTINE),
    ]
)
