# pylint: disable=C0301

"""E0626_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUBROUTINE_FLOWERBOX"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToRandom(PRIMARY_TEMP_7000, 101),
        CompareVarToConst(PRIMARY_TEMP_7000, 80),
        JmpIfComparisonResultIsLesser(["EVENT_626_grant_item_1_ret"]),
        SetVarToConst(ITEM_ID, FlowerBox),
        JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
        Return(identifier="EVENT_626_grant_item_1_ret"),
    ]
)
