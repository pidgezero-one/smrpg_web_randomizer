# pylint: disable=C0301

"""E0563_SUMMONS_HUSBAND_IN_ROSE_TOWN_COUPLES_HOUSE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(FOREST_LIBERATED, ["EVENT_261_1"]),
        PauseActionScript(NPC_0),
        SetSyncActionScript(NPC_0, A0119_SLOW_SEQUENCE_LOOP),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
