# pylint: disable=C0301

"""E0240_FREESTANDING_2_GRANT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 41, ["EVENT_240_room_41_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 79, ["EVENT_240_room_79_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 125, ["EVENT_240_room_125_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 187, ["EVENT_240_room_187_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 207, ["EVENT_240_room_207_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 322, ["EVENT_240_room_322_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 358, ["EVENT_240_room_358_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 378, ["EVENT_240_room_378_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 379, ["EVENT_240_room_379_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 380, ["EVENT_240_room_380_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 381, ["EVENT_240_room_381_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 422, ["EVENT_240_room_422_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 457, ["EVENT_240_room_457_logic"]),
        Return(),
        JmpToEvent(
            E1294_COLLECT_FREESTANDING_SMALL_FROG_COIN,
            identifier="EVENT_240_room_41_logic"),
        JmpToEvent(
            E2822_ASYNC_NO_ANIMATION_MUSHROOM, identifier="EVENT_240_room_79_logic"
        ),
        JmpToEvent(
            E1293_COLLECT_FREESTANDING_SMALL_COIN, identifier="EVENT_240_room_125_logic"
        ),
        JmpToEvent(E3238_FREESTANDING_FROG_COIN, identifier="EVENT_240_room_187_logic"),
        JmpToEvent(
            E1293_COLLECT_FREESTANDING_SMALL_COIN, identifier="EVENT_240_room_207_logic"
        ),
        JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_240_room_322_logic"),
        JmpToEvent(E3238_FREESTANDING_FROG_COIN, identifier="EVENT_240_room_358_logic"),
        JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_240_room_378_logic"),
        JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_240_room_379_logic"),
        JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_240_room_380_logic"),
        JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_240_room_381_logic"),
        JmpToEvent(E1801_FREESTANDING_FLOWER, identifier="EVENT_240_room_422_logic"),
        JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_240_room_457_logic"),
    ]
)
