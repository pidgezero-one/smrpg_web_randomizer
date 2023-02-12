# E2122_STAR_HILL_STAR_PIECE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromSpecificLevel(NPC_9, R159_STAR_HILL_AREA_04),
        RemoveObjectFromCurrentLevel(NPC_9),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
    ]
)
