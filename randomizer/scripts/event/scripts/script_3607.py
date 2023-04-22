# pylint: disable=C0301

"""E3607_COIN_DIFFERENTIATOR_NPC_8_THROUGH_15"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(ACTIVE_NPC, 28, ["EVENT_3607_chest_2"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 29, ["EVENT_3607_chest_3"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 30, ["EVENT_3607_chest_4"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 31, ["EVENT_3607_chest_5"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 32, ["EVENT_3607_chest_6"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 33, ["EVENT_3607_chest_7"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 34, ["EVENT_3607_chest_8"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 35, ["EVENT_3607_chest_9"]),
        JmpToEvent(E0237_FREESTANDING_5_GRANT),
        JmpToEvent(E0236_FREESTANDING_6_GRANT, identifier="EVENT_3607_chest_2"),
        JmpToEvent(E0235_FREESTANDING_7_GRANT, identifier="EVENT_3607_chest_3"),
        JmpToEvent(E0234_FREESTANDING_8_GRANT, identifier="EVENT_3607_chest_4"),
        JmpToEvent(E0233_FREESTANDING_9_GRANT, identifier="EVENT_3607_chest_5"),
        JmpToEvent(E0232_FREESTANDING_10_GRANT, identifier="EVENT_3607_chest_6"),
        JmpToEvent(E0231_FREESTANDING_11_GRANT, identifier="EVENT_3607_chest_7"),
        JmpToEvent(E0230_FREESTANDING_12_GRANT, identifier="EVENT_3607_chest_8"),
        JmpToEvent(E0229_FREESTANDING_13_GRANT, identifier="EVENT_3607_chest_9"),
    ]
)
