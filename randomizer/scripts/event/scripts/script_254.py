# pylint: disable=C0301

"""E0254_EXP_STAR_HIT_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(2, identifier="EVENT_254_pause_0"),
        JmpIfBitClear(TEMP_7076_0, ["EVENT_254_ret_5"]),
        JmpIfBitSet(EXP_STAR_BIT_5, ["EVENT_254_ret_5"]),
        ClearBit(EXP_STAR_BIT_6),
        CreatePacketAtObjectCoords(
            packet=P022_RECURSIVE_SPARKLES,
            target_npc=MARIO,
            destinations=["EVENT_254_pause_0"],
        ),
        Return(identifier="EVENT_254_ret_5"),
    ]
)
