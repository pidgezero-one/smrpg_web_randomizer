# pylint: disable=C0301

"""E2455_FOREST_TRUNK_ROOM_WIGGLER_TRUNK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(DIRECTIONAL_7047_1),
        SetBit(DIRECTIONAL_7046_7),
        SetVarToConst(TEMP_70AC, 7),
        RunEventAsSubroutine(E1542_FOREST_MAZE_PIPE),
        SetAsyncActionScript(MARIO, A0362_PLAYER_IN_FOREST_TRUNK_ROOM_WIGGLER_TRUNK),
        EnterArea(
            room_id=R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS,
            face_direction=SOUTH,
            x=10,
            y=84,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
