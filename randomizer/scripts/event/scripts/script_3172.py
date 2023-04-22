# pylint: disable=C0301

"""E3172_SEWERS_3RD_WATER_ROOM_PIPE_TO_STAIR_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 2),
        SetVarToConst(Y_COORD_2, 106),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS,
            face_direction=SOUTH,
            x=2,
            y=42,
            z=0,
            run_entrance_event=True,
        ),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        Return(),
    ]
)
