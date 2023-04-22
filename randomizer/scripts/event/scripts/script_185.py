# pylint: disable=C0301

"""E0185_NPC_QUEST_GRANT_PROGRESSIVE_FIREWORKS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StoreItemAmountTo7000(Fireworks),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_185_set_298"]),
        StoreItemAmountTo7000(ShinyStone),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_185_set_294"]),
        SetVarToConst(FIREWORKS_COUNTER, 5),
        SetVarToConst(ITEM_ID, Fireworks),
        JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
        SetVarToConst(ITEM_ID, CarboCookie, identifier="EVENT_185_set_294"),
        RemoveOneOfItemFromInventory(ShinyStone),
        JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
        SetVarToConst(ITEM_ID, ShinyStone, identifier="EVENT_185_set_298"),
        ApplySolidityModToLevel(
            permanent=True, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=0
        ),
        RemoveObjectFromSpecificLevel(NPC_2, R324_MONSTRO_TOWN_OUTSIDE),
        RemoveOneOfItemFromInventory(Fireworks),
        JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
    ]
)
