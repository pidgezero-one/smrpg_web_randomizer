# pylint: disable=C0301

"""E2434_FOREST_MAZE_TRANSITION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(DIRECTIONAL_7045_2, ["EVENT_2434_set_bit_12"]),
        JmpIfBitSet(DIRECTIONAL_7045_0, ["EVENT_2434_clear_bit_16"]),
        JmpIfBitSet(DIRECTIONAL_7045_1, ["EVENT_2434_clear_bit_16"]),
        JmpIfBitSet(DIRECTIONAL_7045_3, ["EVENT_2434_clear_bit_16"]),
        JmpIfBitSet(DIRECTIONAL_7045_4, ["EVENT_2434_clear_bit_16"]),
        JmpIfBitSet(DIRECTIONAL_7045_6, ["EVENT_2434_clear_bit_16"]),
        JmpIfBitSet(DIRECTIONAL_7045_7, ["EVENT_2434_clear_bit_16"]),
        JmpIfBitSet(DIRECTIONAL_7046_0, ["EVENT_2434_clear_bit_16"]),
        SetBit(DIRECTIONAL_7045_0),
        ClearBit(DIRECTIONAL_7046_1),
        EnterArea(
            room_id=R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09,
            face_direction=SOUTHEAST,
            x=3,
            y=47,
            z=0,
            run_entrance_event=True),
        Return(),
        SetBit(DIRECTIONAL_7045_3, identifier="EVENT_2434_set_bit_12"),
        ClearBit(DIRECTIONAL_7045_2),
        EnterArea(
            room_id=R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09,
            face_direction=SOUTHEAST,
            x=3,
            y=47,
            z=0,
            run_entrance_event=True),
        Return(),
        ClearBit(DIRECTIONAL_7045_0, identifier="EVENT_2434_clear_bit_16"),
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
            face_direction=SOUTHEAST,
            x=3,
            y=47,
            z=0,
            run_entrance_event=True),
        Return(),
    ]
)
