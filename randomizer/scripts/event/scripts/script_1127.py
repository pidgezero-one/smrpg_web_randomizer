# pylint: disable=C0301

"""E1127_SEASIDE_OCCUPIED_HEALTH_STORE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0811_SEASIDE_OCCUPIED_HEALTH_STORE_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
