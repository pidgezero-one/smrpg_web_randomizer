# E2378_TOWER_PARACHUTE_ROOM_HIDDEN_ITEM

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromSpecificLevel(
            NPC_8, R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS
        ),
        RemoveObjectFromCurrentLevel(NPC_8),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        Return(),
    ]
)
