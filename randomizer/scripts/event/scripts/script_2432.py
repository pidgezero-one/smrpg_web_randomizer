# pylint: disable=C0301

"""E2432_FOREST_MAZE_TRANSITION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(DIRECTIONAL_7045_0, ["EVENT_2432_set_bit_14"]),
        JmpIfBitSet(DIRECTIONAL_7045_1, ["EVENT_2432_set_bit_18"]),
        JmpIfBitSet(DIRECTIONAL_7045_3, ["EVENT_2432_set_bit_22"]),
        ClearBit(DIRECTIONAL_7045_0),
        ClearBit(DIRECTIONAL_7045_1),
        ClearBit(DIRECTIONAL_7045_2),
        ClearBit(DIRECTIONAL_7045_3),
        ClearBit(DIRECTIONAL_7045_4),
        ClearBit(DIRECTIONAL_7045_6),
        ClearBit(DIRECTIONAL_7045_7),
        ClearBit(DIRECTIONAL_7046_0),
        ClearBit(DIRECTIONAL_7046_1),
        EnterArea(
            room_id=R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09,
            face_direction=NORTHEAST,
            x=3,
            y=61,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        SetBit(DIRECTIONAL_7045_1, identifier="EVENT_2432_set_bit_14"),
        ClearBit(DIRECTIONAL_7045_0),
        EnterArea(
            room_id=R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09,
            face_direction=NORTHEAST,
            x=3,
            y=61,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        SetBit(DIRECTIONAL_7045_2, identifier="EVENT_2432_set_bit_18"),
        ClearBit(DIRECTIONAL_7045_1),
        EnterArea(
            room_id=R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09,
            face_direction=NORTHEAST,
            x=3,
            y=61,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        SetBit(DIRECTIONAL_7045_4, identifier="EVENT_2432_set_bit_22"),
        ClearBit(DIRECTIONAL_7045_3),
        EnterArea(
            room_id=R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09,
            face_direction=NORTHEAST,
            x=3,
            y=61,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
