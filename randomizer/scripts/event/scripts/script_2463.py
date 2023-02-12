# E2463_STAR_HILL_2ND_ROOM_SUMMON_WEST_SACKIT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_8, R157_STAR_HILL_AREA_03, ["EVENT_2463_remove_from_level_2"]
        ),
        Return(),
        RemoveObjectFromSpecificLevel(
            NPC_8, R157_STAR_HILL_AREA_03, identifier="EVENT_2463_remove_from_level_2"
        ),
        SetSyncActionScript(NPC_8, A0761_STAR_HILL_2ND_ROOM_WEST_SACKIT),
        Return(),
    ]
)
