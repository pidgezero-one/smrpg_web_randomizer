# pylint: disable=C0301

"""E3882_CHEST_DIFFERENTIATOR_NPC_3_4_OR_OTHER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(ACTIVE_NPC, 23, ["EVENT_3882_chest_2"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 24, ["EVENT_3882_chest_3"]),
        JmpToEvent(E0172_CHEST_1_CONTAINER),
        JmpToEvent(E0173_CHEST_2_CONTAINER, identifier="EVENT_3882_chest_2"),
        JmpToEvent(E0174_CHEST_3_CONTAINER, identifier="EVENT_3882_chest_3"),
    ]
)
