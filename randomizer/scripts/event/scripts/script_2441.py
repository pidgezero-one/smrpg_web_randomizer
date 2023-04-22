# pylint: disable=C0301

"""E2441_FOREST_1ST_TRUNK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(DIRECTIONAL_7047_1),
        RunEventAsSubroutine(E1542_FOREST_MAZE_PIPE),
        SetAsyncActionScript(MARIO, A0355_PLAYER_IN_FOREST_1ST_TRUNK),
        EnterArea(
            room_id=R233_FOREST_MAZE_AREA_03_UNDERGROUND,
            face_direction=SOUTH,
            x=3,
            y=38,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
