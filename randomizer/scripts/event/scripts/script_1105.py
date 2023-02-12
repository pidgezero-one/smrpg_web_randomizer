# E1105_TADPOLE_BRIDGE_SUMMON

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_1105_ret_69"]),
        SetBit(TEMP_7043_1),
        ClearBit(TEMP_7044_6),
        ClearBit(TEMP_7043_5),
        ClearBit(TEMP_7043_6),
        EnableControlsUntilReturn([]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASShadowOff(),
                ASObjectMemorySetBit(arg_1=0x0B, bits=[3]),
                ASBounceToXYWithHeight(x=12, y=51, height=0),
                ASPause(1),
                ASFaceNortheast(),
                ASPause(1),
                ASReturn(),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASVisibilityOff(),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASShiftToXYCoords(x=12, y=47),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASVisibilityOff(),
                ASShiftToXYCoords(x=15, y=49),
                ASShiftNortheastPixels(3),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASVisibilityOff(),
                ASShiftToXYCoords(x=14, y=43),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASShiftToXYCoords(x=17, y=45),
                ASShiftNortheastPixels(3),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASShiftToXYCoords(x=16, y=39),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASShiftToXYCoords(x=19, y=41),
                ASShiftNortheastPixels(3),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASShiftToXYCoords(x=18, y=35),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASShiftToXYCoords(x=21, y=37),
                ASShiftNortheastPixels(3),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASBounceToXYWithHeight(x=10, y=33, height=0),
                ASReturn(),
            ],
        ),
        SetSyncActionScript(NPC_0, A0091_BRIDGE_TADPOLE),
        Pause(5),
        SetSyncActionScript(NPC_1, A0092_BRIDGE_TADPOLE),
        Pause(5),
        SetSyncActionScript(NPC_2, A0091_BRIDGE_TADPOLE),
        Pause(5),
        SetSyncActionScript(NPC_3, A0092_BRIDGE_TADPOLE),
        Pause(5),
        SetSyncActionScript(NPC_4, A0091_BRIDGE_TADPOLE),
        Pause(5),
        SetSyncActionScript(NPC_5, A0092_BRIDGE_TADPOLE),
        Pause(5),
        SetSyncActionScript(NPC_6, A0091_BRIDGE_TADPOLE),
        Pause(5),
        SetSyncActionScript(NPC_7, A0092_BRIDGE_TADPOLE),
        Pause(5),
        ClearBit(TEMP_7044_6),
        Set7000ToTappedButton(identifier="EVENT_1105_set_7000_to_tapped_button_41"),
        Pause(1),
        JmpIf7000AnyBitsSet(destinations=["EVENT_1105_set_7000_to_pressed_button_46"]),
        JmpIf7000AnyBitsSet(destinations=["EVENT_1105_action_queue_sync_49"]),
        Jmp(["EVENT_1105_set_7000_to_tapped_button_41"]),
        Set7000ToPressedButton(identifier="EVENT_1105_set_7000_to_pressed_button_46"),
        JmpIf7000AnyBitsSet(destinations=["EVENT_1107_action_queue_async_0"]),
        Jmp(["EVENT_1105_set_7000_to_tapped_button_41"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASShadowOn(),
                ASSetWalkingSpeed(NORMAL),
                ASFaceSouthwest(),
                ASShiftSouthwestPixels(22),
            ],
            identifier="EVENT_1105_action_queue_sync_49",
        ),
        SetSyncActionScript(NPC_0, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        SetSyncActionScript(NPC_1, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        SetSyncActionScript(NPC_2, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        SetSyncActionScript(NPC_3, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        SetSyncActionScript(NPC_4, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        SetSyncActionScript(NPC_5, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        SetSyncActionScript(NPC_6, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        SetSyncActionScript(NPC_7, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        ClearBit(TEMP_7043_1),
        Return(identifier="EVENT_1105_ret_69"),
    ]
)
