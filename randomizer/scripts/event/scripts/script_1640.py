# pylint: disable=C0301

"""E1640_INITIATE_MINECART_FREEPLAY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
        JmpIfBitSet(PAID_FOR_MINECART, ["EVENT_1640_run_dialog_51"]),
        RunDialog(
            dialog_id=DI1126_MINECART_PAYMENT,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        StoreCoinCountTo7000(),
        CompareVarToConst(PRIMARY_TEMP_7000, 10),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1640_store_coin_amount_7000_13"]),
        RunDialog(
            dialog_id=DI1129_MINECART_NO_COIN,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        StoreCoinCountTo7000(identifier="EVENT_1640_store_coin_amount_7000_13"),
        CompareVarToConst(PRIMARY_TEMP_7000, 30),
        JmpIfComparisonResultIsLesser(["EVENT_1640_store_7000_minecart_timer_22"]),
        JmpIfBitClear(TEMP_7042_2, ["EVENT_1640_store_7000_minecart_timer_22"]),
        Set7000ToMinecartTimer(),
        RunDialogForDuration(
            dialog_id=DI1101_MINECART_HIGH_SCORE, duration=0, sync=False
        ),
        RunDialogForDuration(
            dialog_id=DI1173_TROLLEY_RIDE_PAY_PROMPT, duration=1, sync=False
        ),
        JmpIfDialogOptionBOrCSelected(["EVENT_1640_set_37", "EVENT_1640_ret_50"]),
        Jmp(["EVENT_1640_set_34"]),
        Set7000ToMinecartTimer(identifier="EVENT_1640_store_7000_minecart_timer_22"),
        RunDialogForDuration(dialog_id=DI1127_MINECART_CONFIRM, duration=1, sync=False),
        JmpIfDialogOptionBSelected(["EVENT_1640_pause_47"]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        SetBit(TEMP_7042_2),
        StoreCoinCountTo7000(),
        CompareVarToConst(PRIMARY_TEMP_7000, 30),
        JmpIfComparisonResultIsLesser(["EVENT_1640_set_34"]),
        RunDialog(
            dialog_id=DI1130_WAGER_PROMPT,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        RunDialogForDuration(
            dialog_id=DI1131_WAGER_CHOICE,
            duration=1,
            sync=False,
            identifier="EVENT_1640_run_dialog_duration_32",
        ),
        JmpIfDialogOptionBOrCSelected(
            ["EVENT_1640_set_37", "EVENT_1640_run_dialog_45"]
        ),
        SetVarToConst(PRIMARY_TEMP_7000, 10, identifier="EVENT_1640_set_34"),
        ClearBit(MINECART_INITIATE_FREEPLAY),
        Jmp(["EVENT_1640_run_dialog_39"]),
        SetVarToConst(PRIMARY_TEMP_7000, 30, identifier="EVENT_1640_set_37"),
        SetBit(MINECART_INITIATE_FREEPLAY),
        RunDialog(
            dialog_id=DI1132_MINECART_PAYMENT_CONFIRM,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_1640_run_dialog_39",
        ),
        PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
        Dec7000FromCoins(),
        SetBit(TEMP_7044_5),
        SetBit(PAID_FOR_MINECART),
        Return(),
        RunDialog(
            dialog_id=DI1133_WAGER_EXPLANATION,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_1640_run_dialog_45",
        ),
        Jmp(["EVENT_1640_run_dialog_duration_32"]),
        Pause(10, identifier="EVENT_1640_pause_47"),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        Return(identifier="EVENT_1640_ret_50"),
        RunDialog(
            dialog_id=DI1134_MINECART_ALREADY_PAID,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_1640_run_dialog_51",
        ),
        SetBit(TEMP_7044_5),
        Return(),
    ]
)
