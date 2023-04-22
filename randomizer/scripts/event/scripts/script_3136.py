# pylint: disable=C0301

"""E3136_SEWERS_OVERWORLD_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 5),
        SetVarToConst(Y_COORD_2, 20),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R062_KERO_SEWERS_AREA_01_WATER_ROOM_WSAVE,
            face_direction=SOUTH,
            x=5,
            y=90,
            z=4,
            run_entrance_event=True,
        ),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        Return(),
    ]
)
