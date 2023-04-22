# pylint: disable=C0301

"""E1106_TADPOLE_BRIDGE_SUMMON"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_1106_ret_56"]),
        SetBit(TEMP_7043_1),
        EnableControlsUntilReturn([]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASBounceToXYWithHeight(x=22, y=32, height=4),
                ASPause(1),
                ASFaceSouthwest(),
                ASPause(1),
                ASReturn(),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASShiftToXYCoords(x=12, y=47),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=15, y=49),
                ASWalkNortheastPixels(3),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASShiftToXYCoords(x=14, y=43),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASShiftToXYCoords(x=17, y=45),
                ASWalkNortheastPixels(3),
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
                ASWalkNortheastPixels(3),
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
                ASWalkNortheastPixels(3),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        SetSyncActionScript(NPC_7, A0092_BRIDGE_TADPOLE),
        Pause(5),
        SetSyncActionScript(NPC_6, A0091_BRIDGE_TADPOLE),
        Pause(5),
        SetSyncActionScript(NPC_5, A0092_BRIDGE_TADPOLE),
        Pause(5),
        SetSyncActionScript(NPC_4, A0091_BRIDGE_TADPOLE),
        Pause(5),
        SetSyncActionScript(NPC_3, A0092_BRIDGE_TADPOLE),
        Pause(5),
        SetSyncActionScript(NPC_2, A0091_BRIDGE_TADPOLE),
        Pause(5),
        SetSyncActionScript(NPC_1, A0092_BRIDGE_TADPOLE),
        Pause(5),
        SetSyncActionScript(NPC_0, A0091_BRIDGE_TADPOLE),
        Pause(5),
        Set7000ToTappedButton(identifier="EVENT_1106_set_7000_to_tapped_button_28"),
        Pause(1),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_1106_set_7000_to_pressed_button_33"]
        ),
        JmpIf7000AnyBitsSet(bits=[], destinations=["EVENT_1106_action_queue_sync_36"]),
        Jmp(["EVENT_1106_set_7000_to_tapped_button_28"]),
        Set7000ToPressedButton(identifier="EVENT_1106_set_7000_to_pressed_button_33"),
        JmpIf7000AnyBitsSet(bits=[], destinations=["EVENT_1106_action_queue_async_57"]),
        Jmp(["EVENT_1106_set_7000_to_tapped_button_28"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASShadowOn(),
                ASSetWalkingSpeed(NORMAL),
                ASFaceNortheast(),
                ASWalkNortheastPixels(22),
                ASReturn(),
            ],
            identifier="EVENT_1106_action_queue_sync_36",
        ),
        SetSyncActionScript(NPC_7, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        SetSyncActionScript(NPC_6, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        SetSyncActionScript(NPC_5, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        SetSyncActionScript(NPC_4, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        SetSyncActionScript(NPC_3, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        SetSyncActionScript(NPC_2, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        SetSyncActionScript(NPC_1, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        SetSyncActionScript(NPC_0, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        ClearBit(TEMP_7043_1),
        Return(identifier="EVENT_1106_ret_56"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASShadowOn(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASObjectMemorySetBit(arg_1=0x0B, bits=[3]),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(96),
                ASWalkSouthwestSteps(2),
                ASSetSolidityBits(cant_pass_walls=True),
                ASWalkSouthwestSteps(1),
                ASPause(1),
                ASFaceSouthwest(),
                ASResetProperties(),
                ASSetWalkingSpeed(NORMAL),
            ],
            identifier="EVENT_1106_action_queue_async_57",
        ),
        Jmp(["EVENT_1107_set_7000_to_tapped_button_2"]),
    ]
)
