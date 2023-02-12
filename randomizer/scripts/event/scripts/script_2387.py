# E2387_BEAN_VALLEY_BOSS_PRIZE_PICKUP

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromCurrentLevel(NPC_3),
        RemoveObjectFromSpecificLevel(NPC_3, R254_BEAN_VALLEY_SMILAX_AREA),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        Return(),
    ]
)
