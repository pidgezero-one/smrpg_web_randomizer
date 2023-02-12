# E2475_STAR_HILL_3RD_ROOM_SUMMON_SACKIT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_0, R159_STAR_HILL_AREA_04, ["EVENT_2475_remove_from_level_2"]
        ),
        Return(),
        RemoveObjectFromSpecificLevel(
            NPC_0, R159_STAR_HILL_AREA_04, identifier="EVENT_2475_remove_from_level_2"
        ),
        SetSyncActionScript(NPC_0, A0756_STAR_HILL_3RD_ROOM_SACKIT),
        Return(),
    ]
)
