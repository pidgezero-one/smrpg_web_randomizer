# pylint: disable=C0301

"""E2805_TOWER_APPRENTICE_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_5,
            R198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP,
            ["EVENT_2805_fade_in_from_black_async_2"]),
        ActionQueueAsync(
            target=NPC_5, subscript=[ASSetWalkingSpeed(FASTEST), ASWalkNorthPixels(8)]
        ),
        FadeInFromBlack(sync=False, identifier="EVENT_2805_fade_in_from_black_async_2"),
        Return(),
    ]
)
