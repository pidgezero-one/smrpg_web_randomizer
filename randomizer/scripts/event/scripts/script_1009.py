# pylint: disable=C0301

"""E1009_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(RUN_AWAY, ["EVENT_1008_set_temp_action_script_sync_7"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_287_reset_and_choose_game_0"]),
        RemoveObjectFromCurrentLevel(MEM_70A8),
        JmpIfBitSet(TEMP_704A_2, ["EVENT_1010_clear_bit_7"]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
