# pylint: disable=C0301

"""E3139_SEWERS_4_RAT_ROOM_PIPE_TO_1ST_WATER_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 20),
        SetVarToConst(Y_COORD_2, 100),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES,
            face_direction=SOUTH,
            x=14,
            y=30,
            z=4,
            run_entrance_event=True),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        Return(),
    ]
)
