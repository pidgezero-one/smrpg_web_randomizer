# E2359_ABYSS_1ST_SAVE_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SummonObjectToSpecificLevel(NPC_10, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
        SummonObjectToSpecificLevel(NPC_11, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
        SummonObjectToSpecificLevel(NPC_12, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
        SummonObjectToSpecificLevel(NPC_13, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
        SummonObjectToSpecificLevel(NPC_14, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
        SummonObjectToSpecificLevel(NPC_15, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_2359_set_9"]),
        JmpIfVarEqualsConst(FACTORY_FALL_1, 219, ["EVENT_2359_set_13"]),
        SetVarToConst(FACTORY_FALL_2, 24, identifier="EVENT_2359_set_9"),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASShiftToXYCoords(x=8, y=70),
                ASShiftNortheastPixels(6),
                ASShiftZDownPixels(11),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[ASShiftToXYCoords(x=8, y=69), ASShiftZDownPixels(11)],
        ),
        Jmp(["EVENT_2359_set_16"]),
        SetVarToConst(FACTORY_FALL_2, 0, identifier="EVENT_2359_set_13"),
        ActionQueueSync(
            target=NPC_0, subscript=[ASShiftSouthwestPixels(4), ASShiftZDownPixels(11)]
        ),
        ActionQueueAsync(
            target=NPC_1, subscript=[ASShiftSouthwestPixels(10), ASShiftZDownPixels(11)]
        ),
        SetVarToConst(FACTORY_FALL_1, 220, identifier="EVENT_2359_set_16"),
        RunBackgroundEvent(
            event_id=E2379_ABYSS_1ST_SAVE_ROOM_BACKGROUND, return_on_level_exit=True
        ),
        JmpIfBitClear(TEMP_7044_7, ["EVENT_2359_fade_in_from_black_async_22"]),
        RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE),
        ClearBit(TEMP_7044_4),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2359_ret_21"]),
        RunEventAsSubroutine(E3915_FACTORY_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_2359_ret_21"),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2359_fade_in_from_black_async_22"
        ),
        Return(),
        SetVarToConst(FACTORY_FALL_1, 220, identifier="EVENT_2359_set_24"),
        SetVarToConst(FACTORY_FALL_2, 0),
        ActionQueueSync(
            target=NPC_0, subscript=[ASShiftSouthwestPixels(4), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_1, subscript=[ASShiftSouthwestPixels(10), ASShiftZDownPixels(11)]
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASTransferToXYZF(x=7, y=81, z=0, direction=EAST),
                ASOverwriteSolidity(),
            ],
        ),
        FreezeCamera(),
        FadeInFromBlack(sync=False),
        SetAsyncActionScript(MARIO, A0414_PLAYER_ENTER_ANGLED_JUMPING_POSE),
        SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        RunBackgroundEvent(
            event_id=E2379_ABYSS_1ST_SAVE_ROOM_BACKGROUND, return_on_level_exit=True
        ),
        UnfreezeCamera(),
        Return(),
        SetVarToConst(FACTORY_FALL_1, 220, identifier="EVENT_2359_set_37"),
        SetVarToConst(FACTORY_FALL_2, 24),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASShiftToXYCoords(x=8, y=70),
                ASShiftNortheastPixels(6),
                ASShiftZDownPixels(11),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[ASShiftToXYCoords(x=8, y=69), ASShiftZDownPixels(11)],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASTransferToXYZF(x=9, y=74, z=0, direction=EAST),
                ASOverwriteSolidity(),
            ],
        ),
        FreezeCamera(),
        FadeInFromBlack(sync=False),
        SetAsyncActionScript(MARIO, A0415_PLAYER_ENTER_ANGLED_JUMPING_POSE),
        SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        RunBackgroundEvent(
            event_id=E2379_ABYSS_1ST_SAVE_ROOM_BACKGROUND, return_on_level_exit=True
        ),
        UnfreezeCamera(),
        Return(),
    ]
)
