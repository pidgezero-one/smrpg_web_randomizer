# pylint: disable=C0301

"""E1432_RESCUE_TOAD_EXTENDED"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetSyncActionScript(
            NPC_7, A0563_WHILE_RECRUITABLE_CHARACTER_CAPTIVE_IN_MUSHROOM_WAY_2
        ),
        SetAsyncActionScript(
            NPC_8, A0563_WHILE_RECRUITABLE_CHARACTER_CAPTIVE_IN_MUSHROOM_WAY_2
        ),
        SetSyncActionScript(NPC_7, A0535_MUSHROOM_WAY_2_RECRUITABLE_CHARACTER),
        SetSyncActionScript(NPC_8, A0535_MUSHROOM_WAY_2_RECRUITABLE_CHARACTER),
        EnableObjectTrigger(NPC_7),
        Return(),
    ]
)
