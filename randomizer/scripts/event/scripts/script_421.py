# pylint: disable=C0301

"""E0421_PIPE_VAULT_PIPES_ROOM_EXIT_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_7044_6),
        SetVarToConst(X_COORD_2, 15),
        SetVarToConst(Y_COORD_2, 34),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R129_PIPE_VAULT_AREA_05,
            face_direction=NORTHEAST,
            x=12,
            y=126,
            z=1,
            run_entrance_event=True),
        JmpToEvent(E0269_PIPE_UP_SUBROUTINE),
    ]
)
