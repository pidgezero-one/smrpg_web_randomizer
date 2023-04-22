# pylint: disable=C0301

"""E3823_YOSTER_ISLE_GOALPOST_ITEM_GRANTER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromCurrentLevel(NPC_16),
        RemoveObjectFromSpecificLevel(NPC_16, R034_YOSTER_ISLE),
        RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
        Return(),
    ]
)
