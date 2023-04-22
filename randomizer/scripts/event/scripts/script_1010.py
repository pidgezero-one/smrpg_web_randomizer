# pylint: disable=C0301

"""E1010_SHYSTER_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(GAME_OVER, ["EVENT_287_reset_and_choose_game_0"]),
        CopyVarToVar(from_var=TEMP_70A9, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
        RemoveObjectAt70A8FromCurrentLevel(),
        RemoveObjectFromCurrentLevel(MEM_70A8),
        JmpIfBitSet(TEMP_704A_2, ["EVENT_1010_clear_bit_7"]),
        FadeInFromBlack(sync=False),
        ClearBit(TEMP_704A_2, identifier="EVENT_1010_clear_bit_7"),
        Return(),
    ]
)
