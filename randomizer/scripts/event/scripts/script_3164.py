# pylint: disable=C0301

"""E3164_SEWERS_TUTORIAL_ROOM_PIPE_TO_FIRST_WATER_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 14),
        SetVarToConst(Y_COORD_2, 90),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES,
            face_direction=SOUTH,
            x=12,
            y=26,
            z=8,
            run_entrance_event=True),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        Return(),
    ]
)
