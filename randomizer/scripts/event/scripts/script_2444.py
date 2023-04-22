# pylint: disable=C0301

"""E2444_FOREST_PREMAZE_SAVE_ROOM_TRUNK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(DIRECTIONAL_7047_1),
        SetVarToConst(X_COORD_2, 6),
        SetVarToConst(Y_COORD_2, 40),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R235_FOREST_MAZE_AREA_08_UNDERGROUND,
            face_direction=SOUTH,
            x=28,
            y=110,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
