# E2459_STAR_HILL_1ST_ROOM_SUMMON_NORTHWEST_SACKIT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_7, R158_STAR_HILL_AREA_02, ["EVENT_2459_remove_from_level_2"]
        ),
        Return(),
        RemoveObjectFromSpecificLevel(
            NPC_7, R158_STAR_HILL_AREA_02, identifier="EVENT_2459_remove_from_level_2"
        ),
        SetSyncActionScript(NPC_7, A0748_STAR_HILL_1ST_ROOM_NORTHWEST_SACKIT),
        Return(),
    ]
)
