# pylint: disable=C0301

"""E0226_NPC_QUEST_7_GRANT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_226_room_7_logic"]),
        Return(),
        SetVarToConst(PRIMARY_TEMP_7000, 20, identifier="EVENT_226_room_7_logic"),
        JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
        Return(),
    ]
)
