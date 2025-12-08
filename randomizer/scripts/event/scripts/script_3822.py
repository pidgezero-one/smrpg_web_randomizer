# pylint: disable=C0301

"""E3822_ROSE_TOWN_SIGN_ITEM_GRANTER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromSpecificLevel(NPC_13, R084_ROSE_TOWN_OUTSIDE),
        RemoveObjectFromSpecificLevel(NPC_3, R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 84, ["EVENT_3822_remove_from_current_level_6"]
        ),
        RemoveObjectFromCurrentLevel(NPC_3),
        Jmp(["EVENT_3822_remove_from_current_level_5"]),
        RemoveObjectFromCurrentLevel(
            NPC_13, identifier="EVENT_3822_remove_from_current_level_6"
        ),
        JmpToEvent(
            E0178_NPC_QUEST_1_CONTAINER,
            identifier="EVENT_3822_remove_from_current_level_5"),
    ]
)
