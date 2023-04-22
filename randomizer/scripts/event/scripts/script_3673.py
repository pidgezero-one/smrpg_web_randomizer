# pylint: disable=C0301

"""E3673_NIMBUS_LIBERATED_TOWN_SQUARE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_704C_0),
        ClearBit(GUEST_DROPPED_OFF),
        SetTempAsyncActionScript(NPC_5, A0804_INC_PALETTE_ROW_15),
        SetAsyncActionScript(NPC_6, A0803_INC_PALETTE_ROW),
        SetAsyncActionScript(NPC_1, A0807_INC_PALETTE_ROW_2),
        SetAsyncActionScript(NPC_3, A0803_INC_PALETTE_ROW),
        ActionQueueSync(target=NPC_1, subscript=[ASSetPriority(2)]),
        ActionQueueSync(target=NPC_2, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_3, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_5, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_6, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_7, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_8, subscript=[ASSetPriority(3)]),
        ActionQueueAsync(target=NPC_9, subscript=[ASSetPriority(3), ASShadowOff()]),
        JmpIfBitSet(TEMP_7042_0, ["EVENT_3673_fade_in_from_black_sync_17"]),
        FadeInFromBlack(sync=False),
        Return(),
        FadeInFromBlack(sync=True, identifier="EVENT_3673_fade_in_from_black_sync_17"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(height=132, silent=True),
                ASWalk1StepNortheast(),
                ASFloatingOn(),
                ASWalkNortheastSteps(2),
            ],
        ),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        PauseScriptUntilEffectDone(),
        ClearBit(TEMP_7042_0),
        Return(),
    ]
)
