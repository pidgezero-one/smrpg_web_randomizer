# E0628_MARRYMORE_KITCHEN_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(target=NPC_0, subscript=[ASSetPriority(3)]),
        RunEventAsSubroutine(E0796_MARRYMORE_KITCHEN_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
