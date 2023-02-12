# E2462_STAR_HILL_2ND_ROOM_SUMMON_EAST_SACKIT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_7, R157_STAR_HILL_AREA_03, ["EVENT_2462_remove_from_level_2"]
        ),
        Return(),
        RemoveObjectFromSpecificLevel(
            NPC_7, R157_STAR_HILL_AREA_03, identifier="EVENT_2462_remove_from_level_2"
        ),
        SetSyncActionScript(NPC_7, A0760_STAR_HILL_2ND_ROOM_EAST_SACKIT),
        Return(),
    ]
)
