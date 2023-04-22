# pylint: disable=C0301

"""E0251_NPC_QUEST_3_GRANT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_251_room_7_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 34, ["EVENT_251_room_34_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 74, ["EVENT_251_room_74_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 154, ["EVENT_251_room_154_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 190, ["EVENT_251_room_190_191_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 191, ["EVENT_251_room_190_191_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 336, ["EVENT_251_room_336_logic"]),
        Return(),
        SetVarToConst(PRIMARY_TEMP_7000, 5, identifier="EVENT_251_room_7_logic"),
        JmpToEvent(E0158_NPC_QUEST_GRANT_MULTI_FROG_COIN),
        SetVarToConst(ITEM_ID, YoshiCookie, identifier="EVENT_251_room_34_logic"),
        JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
        JmpToEvent(
            E3097_JUICE_BAR_CARD_NPC_GRANT, identifier="EVENT_251_room_74_logic"
        ),
        JmpToEvent(E3931_GET_SHOES, identifier="EVENT_251_room_154_logic"),
        JmpToEvent(
            E0157_NPC_QUEST_GRANT_1_FROG_COIN, identifier="EVENT_251_room_190_191_logic"
        ),
        SetVarToConst(ITEM_ID, FryingPan, identifier="EVENT_251_room_336_logic"),
        JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
    ]
)
