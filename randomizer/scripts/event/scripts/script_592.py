# pylint: disable=C0301

"""E0592_MINES_BOSS_ROOM_LOADER_BEFORE_DEFEAT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            POST_MINES_LEVEL_MODS_COMPLETED, ["EVENT_257_fade_in_from_black_async_0"]
        ),
        ActionQueueSync(target=NPC_4, subscript=[ASSetPriority(2)]),
        ActionQueueSync(target=NPC_5, subscript=[ASSetPriority(2)]),
        ActionQueueSync(target=NPC_6, subscript=[ASSetPriority(2)]),
        ActionQueueSync(target=NPC_1, subscript=[ASSetPriority(3), ASVisibilityOff()]),
        ActionQueueSync(target=NPC_2, subscript=[ASSetPriority(3), ASVisibilityOff()]),
        ActionQueueAsync(target=NPC_3, subscript=[ASSetPriority(3), ASVisibilityOff()]),
        JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["EVENT_257_fade_in_from_black_async_0"]),
        RunBackgroundEvent(
            event_id=E0596_MINES_BOSS_ROOM_BACKGROUND_EXPLOSIONS,
            return_on_level_exit=True,
        ),
        FadeInFromBlack(sync=False),
        RunEventAsSubroutine(E0788_MINES_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
        Return(),
    ]
)
