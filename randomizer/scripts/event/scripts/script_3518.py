# pylint: disable=C0301

"""E3518_CHEST_DIFFERENTIATOR_NPC_2_3_4_5_6_OR_OTHER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(ACTIVE_NPC, 22, ["EVENT_3518_chest_2"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 23, ["EVENT_3518_chest_3"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 24, ["EVENT_3518_chest_4"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 25, ["EVENT_3518_chest_5"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 26, ["EVENT_3518_chest_6"]),
        JmpToEvent(E1936_KEEP_ROTATING_ROOM_CHEST_1),
        JmpToEvent(E1937_KEEP_ROTATING_ROOM_CHEST_2, identifier="EVENT_3518_chest_2"),
        JmpToEvent(E1938_KEEP_ROTATING_ROOM_CHEST_3, identifier="EVENT_3518_chest_3"),
        JmpToEvent(E1939_KEEP_ROTATING_ROOM_CHEST_4, identifier="EVENT_3518_chest_4"),
        JmpToEvent(E1940_KEEP_ROTATING_ROOM_CHEST_5, identifier="EVENT_3518_chest_5"),
        JmpToEvent(E1941_KEEP_ROTATING_ROOM_CHEST_6, identifier="EVENT_3518_chest_6"),
    ]
)
