# pylint: disable=C0301

"""E3087_PROGRESSIVE_EGG_UPGRADE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StoreItemAmountTo7000(MysteryEgg),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3087_set_298"]),
        StoreItemAmountTo7000(LambsLure),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3087_set_294"]),
        StoreItemAmountTo7000(SheepAttack),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3087_set_298___"]),
        SetVarToConst(ITEM_ID, MysteryEgg),
        JmpToEvent(E0892_CHEST_EGG_PACKET),
        SetVarToConst(ITEM_ID, SheepAttack, identifier="EVENT_3087_set_298___"),
        RemoveOneOfItemFromInventory(SheepAttack),
        JmpToEvent(E0892_CHEST_EGG_PACKET),
        Return(),
        SetVarToConst(ITEM_ID, SheepAttack, identifier="EVENT_3087_set_294"),
        RemoveOneOfItemFromInventory(LambsLure),
        JmpToEvent(E0892_CHEST_EGG_PACKET),
        SetVarToConst(ITEM_ID, LambsLure, identifier="EVENT_3087_set_298"),
        RemoveOneOfItemFromInventory(MysteryEgg),
        JmpToEvent(E0892_CHEST_EGG_PACKET),
    ]
)
