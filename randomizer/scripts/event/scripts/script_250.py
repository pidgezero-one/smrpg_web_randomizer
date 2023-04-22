# pylint: disable=C0301

"""E0250_NPC_QUEST_4_GRANT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_250_room_7_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 34, ["EVENT_250_room_34_logic"]),
        Return(),
        SetVarToConst(PRIMARY_TEMP_7000, 10, identifier="EVENT_250_room_7_logic"),
        JmpToEvent(E0158_NPC_QUEST_GRANT_MULTI_FROG_COIN),
        SetVarToConst(ITEM_ID, YoshiCookie, identifier="EVENT_250_room_34_logic"),
        JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
        Return(),
    ]
)
