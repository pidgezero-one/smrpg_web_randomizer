# E3100_PROGRESSIVE_FIREWORKS_CHEST_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StoreItemAmountTo7000(Fireworks),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3100_set_298"]),
        StoreItemAmountTo7000(ShinyStone),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3100_set_294"]),
        SetVarToConst(FIREWORKS_COUNTER, 5),
        SetVarToConst(ITEM_ID, Fireworks),
        JmpToEvent(E0883_CHEST_ITEM_BAG_PACKET),
        Return(),
        SetVarToConst(ITEM_ID, CarboCookie, identifier="EVENT_3100_set_294"),
        RemoveOneOfItemFromInventory(ShinyStone),
        JmpToEvent(E0883_CHEST_ITEM_BAG_PACKET),
        Return(),
        SetVarToConst(ITEM_ID, ShinyStone, identifier="EVENT_3100_set_298"),
        ApplySolidityModToLevel(
            permanent=True, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=0
        ),
        RemoveObjectFromSpecificLevel(NPC_2, R324_MONSTRO_TOWN_OUTSIDE),
        RemoveOneOfItemFromInventory(Fireworks),
        JmpToEvent(E0883_CHEST_ITEM_BAG_PACKET),
        Return(),
    ]
)
