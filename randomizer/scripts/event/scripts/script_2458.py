# E2458_STAR_HILL_1ST_ROOM_SUMMON_NORTH_SACKIT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_6, R158_STAR_HILL_AREA_02, ["EVENT_2458_remove_from_level_2"]
        ),
        Return(),
        RemoveObjectFromSpecificLevel(
            NPC_6, R158_STAR_HILL_AREA_02, identifier="EVENT_2458_remove_from_level_2"
        ),
        SetSyncActionScript(NPC_6, A0747_STAR_HILL_1ST_ROOM_NORTH_SACKIT),
        Return(),
    ]
)
