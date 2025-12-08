# pylint: disable=C0301

"""E0418_PIPE_VAULT_PIPES_ROOM_ENTRANCE_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_7044_3),
        SetVarToConst(X_COORD_2, 5),
        SetVarToConst(Y_COORD_2, 54),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R127_PIPE_VAULT_AREA_02,
            face_direction=SOUTHWEST,
            x=30,
            y=18,
            z=7,
            run_entrance_event=True),
        JmpToEvent(E0270_TRAMPOLINE_OR_PIPE_SUBROUTINE),
    ]
)
