# E0303_MUSHROOM_KINGDOM_JUMPING_KID

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                )
            ],
        ),
        StartAsyncEmbeddedActionScript(
            target=NPC_0,
            prefix=0xF1,
            subscript=[
                ASFloatingOn(),
                ASJumpToHeight(height=0, silent=True),
                ASPause(
                    1,
                    identifier="EVENT_303_start_embedded_action_script_async_F1_1_SUBSCRIPT_pause_2",
                ),
                ASJmpIfObjectInAir(
                    NPC_0,
                    [
                        "EVENT_303_start_embedded_action_script_async_F1_1_SUBSCRIPT_pause_2"
                    ],
                ),
            ],
        ),
        RunDialog(
            dialog_id=DI0541_JUMPING_KID,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfDialogOptionBSelected(["EVENT_303_run_event_as_subroutine_12"]),
        RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        SetSyncActionScript(NPC_0, A0023_FAST_REPEATED_JUMPING),
        RunDialog(
            dialog_id=DI0545_YEAH,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                )
            ],
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                )
            ],
        ),
        Return(),
        RunEventAsSubroutine(
            E3587_SET_70AE_TO_70A8, identifier="EVENT_303_run_event_as_subroutine_12"
        ),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        RememberLastObject(),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASFixedFCoordOn(),
                ASFaceMario(),
                ASSet700CToObjectCoord(object=NPC_0, coord=COORD_F, pixel=True),
                ASAddConstToVar(PRIMARY_TEMP_700C, 4),
                ASMem700CAndConst(0x0007),
                ASFixedFCoordOff(),
                ASFaceEast7C(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASJumpToHeight(height=0, silent=True),
                ASPause(
                    1, identifier="EVENT_303_action_queue_async_16_SUBSCRIPT_pause_1"
                ),
                ASJmpIfObjectInAir(
                    NPC_0, ["EVENT_303_action_queue_async_16_SUBSCRIPT_pause_1"]
                ),
            ],
        ),
        SetSyncActionScript(NPC_0, A0015_DO_NOTHING),
        RunDialog(
            dialog_id=DI0546_THANKS_A_BUNCH,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                )
            ],
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                )
            ],
        ),
        Return(),
    ]
)
