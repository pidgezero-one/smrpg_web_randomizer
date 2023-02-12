# E2457_STAR_HILL_1ST_ROOM_SUMMON_SOUTH_SACKIT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_5, R158_STAR_HILL_AREA_02, ["EVENT_2457_remove_from_level_2"]
        ),
        Return(),
        RemoveObjectFromSpecificLevel(
            NPC_5, R158_STAR_HILL_AREA_02, identifier="EVENT_2457_remove_from_level_2"
        ),
        SetSyncActionScript(NPC_5, A0746_STAR_HILL_1ST_ROOM_SOUTH_SACKIT),
        Return(),
    ]
)
