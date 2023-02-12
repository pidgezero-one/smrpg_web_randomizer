# E1557_FOREST_MAZE_PAST_TRUNK_AREA_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(DIRECTIONAL_7047_0, ["EVENT_1557_jmp_if_bit_clear_10"]),
        ActionQueueAsync(target=MARIO, subscript=[ASVisibilityOff()]),
        FreezeAllNPCsUntilReturn(),
        FadeInFromBlack(sync=False),
        FreezeCamera(),
        SetAsyncActionScript(MARIO, A0482_FOREST_PLAYER_FALLS_TO_UNDERGROUND),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        UnfreezeAllNPCs(),
        Return(),
        JmpIfBitClear(
            WIGGLER_GOES_DOWN_TRUNK,
            ["EVENT_1557_set_action_script_sync_13"],
            identifier="EVENT_1557_jmp_if_bit_clear_10",
        ),
        FadeInFromBlack(sync=False),
        Return(),
        SetSyncActionScript(
            NPC_0,
            A0036_WIGGLER_GOING_TO_STUMP_TO_SLEEP,
            identifier="EVENT_1557_set_action_script_sync_13",
        ),
        SetSyncActionScript(NPC_1, A0036_WIGGLER_GOING_TO_STUMP_TO_SLEEP),
        SetSyncActionScript(NPC_2, A0036_WIGGLER_GOING_TO_STUMP_TO_SLEEP),
        SetSyncActionScript(NPC_3, A0036_WIGGLER_GOING_TO_STUMP_TO_SLEEP),
        Pause(24),
        FadeInFromBlack(sync=True),
        ActionQueueAsync(target=SCREEN_FOCUS, subscript=[ASWalk1StepWest()]),
        SetBit(WIGGLER_GOES_DOWN_TRUNK),
        Return(),
    ]
)
