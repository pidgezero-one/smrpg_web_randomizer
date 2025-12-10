# pylint: disable=C0301

"""E2645_CASINO_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(FACTORY_BOSS_DEFEATED, ["EVENT_2645_summon_to_level_51_"]),
        JmpIfBitClear(CASINO_WARP_ENABLED, ["EVENT_2645_summon_to_level_51_"]),
        JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 6, ["EVENT_2645_summon_to_level_51"]),
        RemoveObjectFromCurrentLevel(
            NPC_0, identifier="EVENT_2645_summon_to_level_51_"
        ),
        Return(),
        SummonObjectToCurrentLevel(NPC_0, identifier="EVENT_2645_summon_to_level_51"),
        Return(),
    ]
)
