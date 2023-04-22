# pylint: disable=C0301

"""E2084_MARIOS_ROOM_INVISIBLE_ITEM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        RemoveObjectAt70A8FromCurrentLevel(),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromSpecificLevel(NPC_1, R189_MARIOS_PIPEHOUSE),
        Return(),
    ]
)
