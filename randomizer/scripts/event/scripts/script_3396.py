# pylint: disable=C0301

"""E3396_MIDAS_CAVE_PROGRESSIVE_CARD_GRANTER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StoreItemAmountTo7000(AltoCard),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3396_set_298"]),
        StoreItemAmountTo7000(TenorCard),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3396_set_294"]),
        SetVarToConst(ITEM_ID, AltoCard),
        JmpToEvent(E2820_ASYNC_NO_ANIMATION_ITEM),
        SetVarToConst(ITEM_ID, SopranoCard, identifier="EVENT_3396_set_294"),
        RemoveOneOfItemFromInventory(TenorCard),
        JmpToEvent(E2820_ASYNC_NO_ANIMATION_ITEM),
        SetVarToConst(ITEM_ID, TenorCard, identifier="EVENT_3396_set_298"),
        RemoveOneOfItemFromInventory(AltoCard),
        JmpToEvent(E2820_ASYNC_NO_ANIMATION_ITEM),
    ]
)
