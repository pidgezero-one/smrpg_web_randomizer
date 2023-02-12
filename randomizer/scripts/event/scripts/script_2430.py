# E2430_FOREST_PREMAZE_SAVE_ROOM_LOADER

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
        SetBit(DIRECTIONAL_7046_1),
        ActionQueueAsync(
            target=NPC_3, subscript=[ASShiftSouthPixels(4), ASShiftEastPixels(4)]
        ),
        JmpIfBitClear(DIRECTIONAL_7047_0, ["EVENT_2430_jmp_if_bit_clear_27"]),
        ActionQueueAsync(target=MARIO, subscript=[ASVisibilityOff()]),
        FreezeAllNPCsUntilReturn(),
        FadeInFromBlack(sync=False),
        FreezeCamera(),
        SetAsyncActionScript(MARIO, A0482_FOREST_PLAYER_FALLS_TO_UNDERGROUND),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        UnfreezeAllNPCs(),
        Pause(24),
        Jmp(["EVENT_2430_ret_35"]),
        JmpIfBitClear(
            TEMP_7044_7,
            ["EVENT_2430_fade_in_from_black_async_29"],
            identifier="EVENT_2430_jmp_if_bit_clear_27",
        ),
        RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2430_ret_26"]),
        RunEventAsSubroutine(E3896_FOREST_MAZE_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_2430_ret_26"),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2430_fade_in_from_black_async_29"
        ),
        Return(identifier="EVENT_2430_ret_35"),
    ]
)
