# pylint: disable=C0301

"""E0417_PIPE_VAULT_THWOMP_ROOM_EXIT_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_7044_3),
        SetVarToConst(X_COORD_2, 30),
        SetVarToConst(Y_COORD_2, 18),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES,
            face_direction=NORTHEAST,
            x=5,
            y=54,
            z=1,
            run_entrance_event=True),
        Return(),
    ]
)
