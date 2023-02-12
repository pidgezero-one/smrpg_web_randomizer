# E1554_FOREST_FIRST_WIGGLER_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(DIRECTIONAL_7047_0, ["EVENT_1554_fade_in_from_black_sync_10"]),
        ActionQueueAsync(target=MARIO, subscript=[ASVisibilityOff()]),
        FreezeAllNPCsUntilReturn(),
        FadeInFromBlack(sync=False),
        FreezeCamera(),
        SetAsyncActionScript(MARIO, A0482_FOREST_PLAYER_FALLS_TO_UNDERGROUND),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        UnfreezeAllNPCs(),
        Jmp(["EVENT_1554_set_11"]),
        FadeInFromBlack(sync=True, identifier="EVENT_1554_fade_in_from_black_sync_10"),
        SetVarToConst(TEMP_70A9, 20, identifier="EVENT_1554_set_11"),
        StartLoopNTimes(3),
        ActionQueueSync(
            target=MEM_70A9,
            subscript=[ASClearSolidityBits(bit_4=True, cant_walk_through=True)],
        ),
        Inc(TEMP_70A9),
        EndLoop(),
        ActionQueueAsync(
            target=MARIO, subscript=[ASObjectMemorySetBit(arg_1=0x0B, bits=[3])]
        ),
        SetVarToConst(TEMP_70AB, 24),
        RunBackgroundEvent(
            event_id=E1555_FOREST_FIRST_WIGGLER_ROOM_LOADER_CONTD,
            return_on_level_exit=True,
        ),
        Return(),
    ]
)
