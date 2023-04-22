# pylint: disable=C0301

"""E1129_SEASIDE_OCCUPIED_ACCESSORY_SHOP_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0813_SEASIDE_OCCUPIED_ACCESSORY_SHOP_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
