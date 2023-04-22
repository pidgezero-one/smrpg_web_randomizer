# pylint: disable=C0301

"""E3606_CHEST_DIFFERENTIATOR_NPC_1_OR_OTHER_CAMERA_A"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(ACTIVE_NPC, 21, ["EVENT_3606_chest_2"]),
        JmpToEvent(E1538_BANDITS_WAY_STAR_CHEST_CAMERA_AND_DOGS),
        JmpToEvent(E1587_BANDITS_WAY_4_RIGHT_CHEST, identifier="EVENT_3606_chest_2"),
    ]
)
