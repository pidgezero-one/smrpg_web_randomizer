# pylint: disable=C0301

"""E1128_SEASIDE_OCCUPIED_MUSHROOM_BOY_SHOP_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0812_SEASIDE_OCCUPIED_MUSHROOM_BOY_SHOP_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
