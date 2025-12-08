# pylint: disable=C0301

"""E0014_STANDARD_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7044_7, ["EVENT_14_clear_bit_2"]),
        JmpToEvent(E0081_MARIO_LANDS_SUBROUTINE),
        ClearBit(EXP_STAR_BIT_1, identifier="EVENT_14_clear_bit_2"),
        ClearBit(EXP_STAR_BIT_2),
        ClearBit(EXP_STAR_BIT_3),
        ClearBit(EXP_STAR_BIT_4),
        SetVarToConst(COIN_COUNTER_1, 0),
        SetVarToConst(COIN_COUNTER_2, 0),
        SetVarToConst(COIN_COUNTER_3, 0),
        SetVarToConst(COIN_COUNTER_4, 0),
        SetVarToConst(COIN_COUNTER_5, 0),
        SetVarToConst(COIN_COUNTER_6, 0),
        FadeInFromBlack(sync=True),
        JmpIfBitClear(TEMP_7076_0, ["EVENT_14_ret_15"]),
        JmpIfBitSet(EXP_STAR_BIT_5, ["EVENT_14_ret_15"]),
        ClearBit(EXP_STAR_BIT_6),
        CreatePacketAtObjectCoords(
            packet=P022_RECURSIVE_SPARKLES,
            target_npc=MARIO,
            destinations=["EVENT_14_ret_15"]),
        Return(identifier="EVENT_14_ret_15"),
    ]
)
