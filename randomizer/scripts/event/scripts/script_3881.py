# pylint: disable=C0301

"""E3881_CHEST_DIFFERENTIATOR_NPC_1_OR_OTHER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(ACTIVE_NPC, 21, ["EVENT_3881_chest_2"]),
        JmpToEvent(E0172_CHEST_1_CONTAINER),
        JmpToEvent(E0173_CHEST_2_CONTAINER, identifier="EVENT_3881_chest_2"),
    ]
)
