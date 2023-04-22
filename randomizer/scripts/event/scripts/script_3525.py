# pylint: disable=C0301

"""E3525_EMPTY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(ACTIVE_NPC, 21, ["EVENT_3525_chest_2"]),
        JmpToEvent(E0172_CHEST_1_CONTAINER),
        JmpToEvent(E3145_SEWERS_FLIPPABLE_CHEST, identifier="EVENT_3525_chest_2"),
    ]
)
