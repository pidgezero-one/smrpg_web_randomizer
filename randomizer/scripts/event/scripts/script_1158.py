# pylint: disable=C0301

"""E1158_SEASIDE_LIBERATED_WPN_ARM_SHOP_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(SEASIDE_SHED_EMPTIED, ["EVENT_1158_remove_from_current_level_3"]),
        FadeInFromBlack(sync=False),
        Return(),
        RemoveObjectFromCurrentLevel(
            NPC_0, identifier="EVENT_1158_remove_from_current_level_3"
        ),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_3),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
