# E3703_NIMBUS_CASTLE_TWO_LEVEL_CHEST_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 498, ["EVENT_3703_fade_in_from_black_async_7"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_4,
            R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
            ["EVENT_3703_fade_in_from_black_async_7"],
        ),
        ActionQueueSync(target=NPC_4, subscript=[ASSetPriority(3)]),
        FadeInFromBlack(sync=False, identifier="EVENT_3703_fade_in_from_black_async_7"),
        Return(),
    ]
)
