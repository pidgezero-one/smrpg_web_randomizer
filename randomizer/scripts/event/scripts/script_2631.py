# E2631_CASINO_SLOT_MACHINE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TEMP_70AE, 22),
        RunDialog(
            dialog_id=DI3312_CASINO_SLOTS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfDialogOptionBSelected(["EVENT_2631_pause_23"]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        JmpIfBitSet(DIRECTIONAL_7045_7, ["EVENT_2631_store_coin_amount_7000_11"]),
        SetBit(DIRECTIONAL_7045_7),
        RunDialog(
            dialog_id=DI3314_CASINO_SLOTS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfDialogOptionBSelected(["EVENT_2631_pause_16"]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        StoreCoinCountTo7000(identifier="EVENT_2631_store_coin_amount_7000_11"),
        CompareVarToConst(PRIMARY_TEMP_7000, 10),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2631_run_dialog_27"]),
        RunDialog(
            dialog_id=DI3316_CASINO_SLOTS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        Pause(10, identifier="EVENT_2631_pause_16"),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        RunDialog(
            dialog_id=DI3317_CASINO_SLOTS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfDialogOptionBSelected(["EVENT_2631_pause_23"]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        Jmp(["EVENT_2631_store_coin_amount_7000_11"]),
        Pause(10, identifier="EVENT_2631_pause_23"),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        Return(),
        RunDialog(
            dialog_id=DI3315_CASINO_SLOTS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_2631_run_dialog_27",
        ),
        SetVarToConst(PRIMARY_TEMP_7000, 10),
        Dec7000FromCoins(),
        SetBit(TEMP_7043_0),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASOverwriteSolidity(),
                ASSetAllSpeeds(FAST),
                ASWalkToXYCoords(x=1, y=17),
                ASFaceSouth(),
                ASOverwriteSolidity(
                    cant_pass_walls=True,
                    bit_4=True,
                    cant_pass_npcs=True,
                    cant_walk_through=True,
                    bit_7=True,
                ),
                ASSetAllSpeeds(NORMAL),
            ],
        ),
        EnableControls([B]),
        SetSyncActionScript(NPC_4, A0014_FLOATING_CHEST),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetSpriteSequence(
                    index=10, is_mold=True, is_sequence=True, looping=True
                )
            ],
        ),
        Return(),
    ]
)
