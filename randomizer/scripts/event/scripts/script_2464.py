# E2464_STAR_HILL_2ND_ROOM_SUMMON_CENTRAL_SACKIT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_9, R157_STAR_HILL_AREA_03, ["EVENT_2464_remove_from_level_2"]
        ),
        Return(),
        RemoveObjectFromSpecificLevel(
            NPC_9, R157_STAR_HILL_AREA_03, identifier="EVENT_2464_remove_from_level_2"
        ),
        SetSyncActionScript(NPC_9, A0762_STAR_HILL_2ND_ROOM_CENTRAL_SACKIT),
        Return(),
    ]
)
