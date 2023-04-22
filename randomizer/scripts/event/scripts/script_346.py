# pylint: disable=C0301

"""E0346_TOADSTOOLS_ROOM_ITEM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 328, ["EVENT_346_remove_from_current_level_1"]
        ),
        RemoveObjectFromCurrentLevel(NPC_0),
        Jmp(["EVENT_346_remove_from_level_1"]),
        RemoveObjectFromCurrentLevel(
            NPC_7, identifier="EVENT_346_remove_from_current_level_1"
        ),
        RemoveObjectFromSpecificLevel(
            NPC_0,
            R020_MUSHROOM_KINGDOM_CASTLE_TOADSTOOLS_ROOM,
            identifier="EVENT_346_remove_from_level_1",
        ),
        RemoveObjectFromSpecificLevel(
            NPC_7, R328_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_TOADSTOOLS_ROOM
        ),
        JmpToEvent(E0178_NPC_QUEST_1_CONTAINER),
    ]
)
