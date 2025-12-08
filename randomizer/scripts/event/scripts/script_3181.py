# pylint: disable=C0301

"""E3181_SEWERS_WATER_SWITCH_ROOM_PIPE_TO_3RD_WATER_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 11),
        SetVarToConst(Y_COORD_2, 118),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER,
            face_direction=SOUTH,
            x=15,
            y=104,
            z=5,
            run_entrance_event=True),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        Return(),
    ]
)
