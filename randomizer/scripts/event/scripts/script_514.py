# pylint: disable=C0301

"""E0514_GAZ_ITEM_GRANT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(ROSE_TOWN_GAZ_ITEM_GRANTED, ["EVENT_514_gaz_Normal"]),
        SetBit(ROSE_TOWN_GAZ_ITEM_GRANTED),
        JmpToEvent(E0178_NPC_QUEST_1_CONTAINER),
        JmpToEvent(E0516_OCCUPIED_ROSE_TOWN_GAZ, identifier="EVENT_514_gaz_Normal"),
    ]
)
