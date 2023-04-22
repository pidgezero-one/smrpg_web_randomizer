# pylint: disable=C0301

"""E1347_TOWER_HENCHMAN_2_ROOM_HIDDEN_ITEM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromSpecificLevel(
            NPC_1, R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM
        ),
        JmpToEvent(E0178_NPC_QUEST_1_CONTAINER),
    ]
)
