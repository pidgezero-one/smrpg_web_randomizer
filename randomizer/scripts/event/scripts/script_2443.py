# pylint: disable=C0301

"""E2443_FOREST_ROOM_BEFORE_TRUNKS_AREA_TRUNK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(DIRECTIONAL_7047_1),
        SetVarToConst(X_COORD_2, 6),
        SetVarToConst(Y_COORD_2, 110),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R233_FOREST_MAZE_AREA_03_UNDERGROUND,
            face_direction=SOUTH,
            x=26,
            y=36,
            z=0,
            run_entrance_event=True),
        Return(),
    ]
)
