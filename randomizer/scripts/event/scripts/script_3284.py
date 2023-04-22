# pylint: disable=C0301

"""E3284_SHIP_SAVE_ROOMS_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7044_7, ["EVENT_3284_clear_bit_6"]),
        ClearBit(TEMP_7043_0),
        SetVarToConst(TEMP_70AE, 0),
        ClearBit(TEMP_7044_5),
        ClearBit(TEMP_7044_6),
        RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3284_ret_26"]),
        RunEventAsSubroutine(E3906_SHIP_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_3284_ret_26"),
        ClearBit(EXP_STAR_BIT_1, identifier="EVENT_3284_clear_bit_6"),
        ClearBit(EXP_STAR_BIT_2),
        ClearBit(EXP_STAR_BIT_3),
        ClearBit(EXP_STAR_BIT_4),
        SetVarToConst(COIN_COUNTER_1, 0),
        SetVarToConst(COIN_COUNTER_2, 0),
        SetVarToConst(COIN_COUNTER_3, 0),
        SetVarToConst(COIN_COUNTER_4, 0),
        SetVarToConst(COIN_COUNTER_5, 0),
        SetVarToConst(COIN_COUNTER_6, 0),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
