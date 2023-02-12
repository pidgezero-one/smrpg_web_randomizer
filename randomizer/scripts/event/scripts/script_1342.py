# E1342_ELDER_KEY_PRIZE_GRANTER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromSpecificLevel(
            NPC_0, R200_BOOSTER_TOWER_6F_AREA_03_ELDERS_ROOM_WCHOMP
        ),
        RunEventAsSubroutine(E0241_FREESTANDING_1_GRANT),
        Return(),
    ]
)
