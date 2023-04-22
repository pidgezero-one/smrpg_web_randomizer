# pylint: disable=C0301

"""E2460_STAR_HILL_1ST_ROOM_SUMMON_SOUTHEAST_SACKIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_8, R158_STAR_HILL_AREA_02, ["EVENT_2460_remove_from_level_2"]
        ),
        Return(),
        RemoveObjectFromSpecificLevel(
            NPC_8, R158_STAR_HILL_AREA_02, identifier="EVENT_2460_remove_from_level_2"
        ),
        SetSyncActionScript(NPC_8, A0749_STAR_HILL_1ST_ROOM_SOUTHEAST_SACKIT),
        Return(),
    ]
)
