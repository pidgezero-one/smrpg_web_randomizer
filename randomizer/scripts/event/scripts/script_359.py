# pylint: disable=C0301

"""E0359_CHEST_CLONES"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(ACTIVE_NPC, 22, ["EVENT_359_chest_2"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 23, ["EVENT_359_chest_3"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 24, ["EVENT_359_chest_4"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 25, ["EVENT_359_chest_5"]),
        JmpToEvent(E0172_CHEST_1_CONTAINER),
        JmpToEvent(E0173_CHEST_2_CONTAINER, identifier="EVENT_359_chest_2"),
        JmpToEvent(E0174_CHEST_3_CONTAINER, identifier="EVENT_359_chest_3"),
        JmpToEvent(E0175_CHEST_4_CONTAINER, identifier="EVENT_359_chest_4"),
        JmpToEvent(E0176_CHEST_5_CONTAINER, identifier="EVENT_359_chest_5"),
    ]
)
