# E1423_MUSHROOM_WAY_2_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(target=NPC_7, subscript=[ASSetPriority(3), ASReturn()]),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetPriority(3),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASReturn(),
            ],
        ),
        JmpIfBitClear(
            TOAD_IN_MUSHROOM_WAY_1, ["EVENT_1423_remove_from_current_level_7"]
        ),
        JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_2, ["EVENT_1423_remove_from_current_level_7"]),
        JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_3, ["EVENT_1423_remove_from_current_level_7"]),
        FadeInFromBlack(sync=False),
        Return(),
        RemoveObjectFromCurrentLevel(
            NPC_7, identifier="EVENT_1423_remove_from_current_level_7"
        ),
        RemoveObjectFromCurrentLevel(NPC_8),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
