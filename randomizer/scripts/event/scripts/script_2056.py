# pylint: disable=C0301

"""E2056_MONSTRO_LEDGE_ITEM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromSpecificLevel(NPC_0, R324_MONSTRO_TOWN_OUTSIDE),
        JmpToEvent(E0241_FREESTANDING_1_GRANT),
    ]
)
