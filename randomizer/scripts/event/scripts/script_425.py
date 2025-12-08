# pylint: disable=C0301

"""E0425_PIPE_VAULT_RED_ROOM_EXIT_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 7),
        SetVarToConst(Y_COORD_2, 90),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS,
            face_direction=NORTHEAST,
            x=12,
            y=84,
            z=2,
            run_entrance_event=True),
        JmpToEvent(E0269_PIPE_UP_SUBROUTINE),
    ]
)
