# E3642_NIMBUS_EXTERIOR_OCCUPIED_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(
            NIMBUS_MID_BOSS_COMPLETED, ["EVENT_3642_set_temp_action_script_async_5"]
        ),
        ClearBit(TEMP_704C_0),
        ClearBit(GUEST_DROPPED_OFF),
        SetTempAsyncActionScript(
            NPC_5,
            A0804_INC_PALETTE_ROW_15,
            identifier="EVENT_3642_set_temp_action_script_async_5",
        ),
        SetTempAsyncActionScript(NPC_6, A0807_INC_PALETTE_ROW_2),
        SetTempAsyncActionScript(NPC_1, A0806_INC_PALETTE_ROW_3),
        SetTempAsyncActionScript(NPC_3, A0803_INC_PALETTE_ROW),
        ActionQueueSync(target=NPC_1, subscript=[ASSetPriority(2)]),
        ActionQueueSync(target=NPC_2, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_3, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_5, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_6, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_7, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_10, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_8, subscript=[ASSetPriority(3)]),
        ActionQueueAsync(target=NPC_9, subscript=[ASSetPriority(3)]),
        JmpIfBitSet(TEMP_704C_0, ["EVENT_3584_ret_0"]),
        JmpIfBitSet(TEMP_7042_0, ["EVENT_3642_fade_in_from_black_sync_24"]),
        FadeInFromBlack(sync=False),
        Return(),
        FadeInFromBlack(sync=True, identifier="EVENT_3642_fade_in_from_black_sync_24"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(132),
                ASWalk1StepNortheast(),
                ASFloatingOn(),
                ASShiftNortheastSteps(2),
            ],
        ),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        PauseScriptUntilEffectDone(),
        ClearBit(TEMP_7042_0),
        Return(),
    ]
)
