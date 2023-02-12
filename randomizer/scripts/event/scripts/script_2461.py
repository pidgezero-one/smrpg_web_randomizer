# E2461_STAR_HILL_2ND_ROOM_SUMMON_NORTH_SACKIT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_6, R157_STAR_HILL_AREA_03, ["EVENT_2461_remove_from_level_2"]
        ),
        Return(),
        RemoveObjectFromSpecificLevel(
            NPC_6, R157_STAR_HILL_AREA_03, identifier="EVENT_2461_remove_from_level_2"
        ),
        SetSyncActionScript(NPC_6, A0759_STAR_HILL_2ND_ROOM_NORTH_SACKIT),
        Return(),
    ]
)
