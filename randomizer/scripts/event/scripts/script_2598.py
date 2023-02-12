# E2598_FOREST_SECRET_ENTRANCE_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(DIRECTIONAL_7045_0),
        ClearBit(DIRECTIONAL_7045_1),
        ClearBit(DIRECTIONAL_7045_2),
        ClearBit(DIRECTIONAL_7045_3),
        ClearBit(DIRECTIONAL_7045_4),
        ClearBit(DIRECTIONAL_7045_5),
        ClearBit(DIRECTIONAL_7045_6),
        ClearBit(DIRECTIONAL_7045_7),
        ClearBit(DIRECTIONAL_7046_0),
        ClearBit(DIRECTIONAL_7046_1),
        ClearBit(EXP_STAR_BIT_1),
        ClearBit(EXP_STAR_BIT_2),
        ClearBit(EXP_STAR_BIT_3),
        ClearBit(EXP_STAR_BIT_4),
        SetVarToConst(COIN_COUNTER_1, 0),
        SetVarToConst(COIN_COUNTER_2, 0),
        SetVarToConst(COIN_COUNTER_3, 0),
        SetVarToConst(COIN_COUNTER_4, 0),
        SetVarToConst(COIN_COUNTER_5, 0),
        SetVarToConst(COIN_COUNTER_6, 0),
        JmpIfBitClear(DIRECTIONAL_7047_0, ["EVENT_2598_fade_in_from_black_async_26"]),
        ActionQueueAsync(target=MARIO, subscript=[ASVisibilityOff()]),
        FadeInFromBlack(sync=False),
        FreezeCamera(),
        SetAsyncActionScript(MARIO, A0482_FOREST_PLAYER_FALLS_TO_UNDERGROUND),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        Return(),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2598_fade_in_from_black_async_26"
        ),
        Return(),
    ]
)
