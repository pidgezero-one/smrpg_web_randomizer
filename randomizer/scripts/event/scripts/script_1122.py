# pylint: disable=C0301

"""E1122_SEASIDE_OCCUPIED_INN_2F_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0808_SEASIDE_OCCUPIED_INN_2F_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
