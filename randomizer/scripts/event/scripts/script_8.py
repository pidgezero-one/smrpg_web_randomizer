# pylint: disable=C0301

"""E0008_SET_70A7_TO_RANDOM_TIER_4_CONSUMABLE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToRandom(PRIMARY_TEMP_7000, 4),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_8_set_3"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_8_set_4"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_8_set_5"]),
        SetVarToConst(ITEM_ID, RedEssence),
        JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
        SetVarToConst(ITEM_ID, KerokeroCola, identifier="EVENT_8_set_3"),
        JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
        SetVarToConst(ITEM_ID, FlowerBox, identifier="EVENT_8_set_4"),
        JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
        SetVarToConst(ITEM_ID, RockCandy, identifier="EVENT_8_set_5"),
        JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
    ]
)
