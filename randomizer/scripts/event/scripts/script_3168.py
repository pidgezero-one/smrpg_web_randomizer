# pylint: disable=C0301

"""E3168_SEWERS_3RD_WATER_ROOM_PIPE_TO_WATER_SWITCH_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 15),
        SetVarToConst(Y_COORD_2, 104),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS,
            face_direction=SOUTH,
            x=11,
            y=118,
            z=0,
            run_entrance_event=True,
        ),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        Return(),
    ]
)
