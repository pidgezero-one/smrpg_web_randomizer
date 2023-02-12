# E0455_RESUMMON_PIPE_VAULT_ENEMIES

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_707C_0),
        SummonObjectToSpecificLevel(NPC_0, R123_PIPE_VAULT_AREA_01),
        SummonObjectToSpecificLevel(NPC_1, R123_PIPE_VAULT_AREA_01),
        SummonObjectToSpecificLevel(NPC_2, R123_PIPE_VAULT_AREA_01),
        SummonObjectToSpecificLevel(NPC_3, R123_PIPE_VAULT_AREA_01),
        SummonObjectToSpecificLevel(NPC_1, R127_PIPE_VAULT_AREA_02),
        SummonObjectToSpecificLevel(NPC_2, R127_PIPE_VAULT_AREA_02),
        SummonObjectToSpecificLevel(NPC_3, R127_PIPE_VAULT_AREA_02),
        SummonObjectToSpecificLevel(NPC_0, R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES),
        SummonObjectToSpecificLevel(NPC_1, R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES),
        SummonObjectToSpecificLevel(NPC_2, R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES),
        SummonObjectToSpecificLevel(NPC_3, R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES),
        SummonObjectToSpecificLevel(NPC_0, R129_PIPE_VAULT_AREA_05),
        SummonObjectToSpecificLevel(NPC_1, R129_PIPE_VAULT_AREA_05),
        SummonObjectToSpecificLevel(NPC_2, R129_PIPE_VAULT_AREA_05),
        SummonObjectToSpecificLevel(NPC_3, R129_PIPE_VAULT_AREA_05),
        SummonObjectToSpecificLevel(NPC_0, R126_PIPE_VAULT_AREA_06_LINE_OF_RED_PIPES),
        SummonObjectToSpecificLevel(NPC_1, R126_PIPE_VAULT_AREA_06_LINE_OF_RED_PIPES),
        SummonObjectToSpecificLevel(
            NPC_12, R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS
        ),
        SummonObjectToSpecificLevel(
            NPC_13, R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS
        ),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 33, ["EVENT_455_set_27"]),
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 20),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASShiftEastPixels(11),
                ASShiftNortheastPixels(4),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASSetVRAMPriority(NORMAL_PRIORITY),
            ],
        ),
        JmpIfBitClear(PIPE_VAULT_GATED, ["EVENT_455_fade_in_from_black_async_23"]),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromSpecificLevel(NPC_1, R055_PIPE_VAULT_ENTRANCE),
        RemoveObjectFromSpecificLevel(NPC_0, R055_PIPE_VAULT_ENTRANCE),
        FadeInFromBlack(sync=False, identifier="EVENT_455_fade_in_from_black_async_23"),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_455_ret_24"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_455_ret_24"]),
        RunEventAsSubroutine(E3900_PIPE_VAULT_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_455_ret_24"),
        RunEventAsSubroutine(
            E0081_MARIO_LANDS_SUBROUTINE,
            identifier="EVENT_455_run_event_as_subroutine_25",
        ),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_455_ret_26"]),
        RunEventAsSubroutine(E3901_YOSTER_ISLE_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_455_ret_26"),
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 52, identifier="EVENT_455_set_27"),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_455_run_event_as_subroutine_25"]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
