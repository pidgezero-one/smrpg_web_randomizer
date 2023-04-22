# pylint: disable=C0301

"""E3610_KEEP_INVISIBLE_FLOOR_COINS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(ACTIVE_NPC, 29, ["EVENT_3610_chest_2"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 30, ["EVENT_3610_chest_3"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 31, ["EVENT_3610_chest_4"]),
        JmpToEvent(E1842_KEEP_INVISIBLE_FLOOR_COIN_1),
        JmpToEvent(E1881_KEEP_INVISIBLE_FLOOR_COIN_2, identifier="EVENT_3610_chest_2"),
        JmpToEvent(E1882_KEEP_INVISIBLE_FLOOR_COIN_3, identifier="EVENT_3610_chest_3"),
        JmpToEvent(E1929_KEEP_INVISIBLE_FLOOR_COIN_4, identifier="EVENT_3610_chest_4"),
    ]
)
